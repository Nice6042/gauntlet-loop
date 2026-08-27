#!/usr/bin/env python3
"""Validate and deterministically package the Gauntlet Loop Agent Skill."""

from __future__ import annotations

import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "gauntlet-loop"
DIST_DIR = ROOT / "dist"
VERSION_PATTERN = re.compile(r"^[0-9]+\.[0-9]+\.[0-9]+$")
TOP_LEVEL_FRONTMATTER_KEY = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):(?:\s|$)")
LOCAL_SKILL_PATH = re.compile(
    r"(?<![A-Za-z0-9._/-])((?:references|templates|schemas|adapters)/[A-Za-z0-9._/-]+)"
)
ALLOWED_FRONTMATTER_KEYS = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
}
REQUIRED_PATHS = (
    "README.md",
    "LICENSE",
    "VERSION",
    "plugin.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    "evals/activation-cases.json",
    "evals/bug-hunt-cases.json",
    "skills/gauntlet-loop/SKILL.md",
    "skills/gauntlet-loop/references/core-protocol.md",
    "skills/gauntlet-loop/references/metrics.md",
    "skills/gauntlet-loop/references/quality-contract.md",
    "skills/gauntlet-loop/references/concurrency.md",
    "skills/gauntlet-loop/references/bug-hunt-protocol.md",
    "skills/gauntlet-loop/templates/owner-intake.md",
    "skills/gauntlet-loop/templates/bug-spec.md",
    "skills/gauntlet-loop/templates/bug-campaign-state.md",
    "skills/gauntlet-loop/schemas/bug-spec.schema.json",
    "skills/gauntlet-loop/schemas/bug-campaign.schema.json",
    "skills/gauntlet-loop/adapters/generic.md",
)
MANIFEST_VERSION_PATHS = (
    ("plugin.json", ("version",)),
    (".claude-plugin/plugin.json", ("version",)),
    (".claude-plugin/marketplace.json", ("plugins", 0, "version")),
    (".codex-plugin/plugin.json", ("version",)),
    (".agents/plugins/marketplace.json", ("plugins", 0, "version")),
)
SECURITY_PATTERNS = (
    ("private-key", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("aws-access-key", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
)
DIST_OUTPUTS = (
    "gauntlet-loop.skill",
    "SHA256SUMS",
    "security-scan.json",
    "VALIDATION_REPORT.txt",
    "RELEASE_STATUS.json",
)


def get_nested(value: object, path: tuple[object, ...]) -> object:
    current = value
    for key in path:
        if isinstance(key, int):
            if not isinstance(current, list) or key >= len(current):
                raise KeyError(path)
            current = current[key]
        else:
            if not isinstance(current, dict) or key not in current:
                raise KeyError(path)
            current = current[key]
    return current


def load_json(relative_path: str, errors: list[str]) -> object | None:
    path = ROOT / relative_path
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON {relative_path}: {exc}")
        return None


def frontmatter(skill_text: str, errors: list[str]) -> str:
    if not skill_text.startswith("---\n"):
        errors.append("SKILL.md must begin with YAML frontmatter")
        return ""
    end = skill_text.find("\n---\n", 4)
    if end < 0:
        errors.append("SKILL.md frontmatter has no closing delimiter")
        return ""
    return skill_text[4:end]


def scalar_from_frontmatter(block: str, key: str) -> str | None:
    lines = block.splitlines()
    for index, line in enumerate(lines):
        match = re.match(rf"^{re.escape(key)}:\s*(.*)$", line)
        if not match:
            continue
        value = match.group(1).strip()
        if value in {">", ">-", "|", "|-"}:
            parts: list[str] = []
            for continuation in lines[index + 1 :]:
                if TOP_LEVEL_FRONTMATTER_KEY.match(continuation):
                    break
                if continuation.startswith((" ", "\t")):
                    stripped = continuation.strip()
                    if stripped:
                        parts.append(stripped)
            return " ".join(parts)
        return value.strip("'\"")
    return None


def metadata_version(block: str) -> str | None:
    match = re.search(r"^metadata:\s*$([\s\S]*?)(?=^[A-Za-z][A-Za-z0-9_-]*:|\Z)", block, re.MULTILINE)
    if not match:
        return None
    version = re.search(r"^\s+version:\s*([^\s#]+)", match.group(1), re.MULTILINE)
    return version.group(1).strip("'\"") if version else None


def validate_frontmatter(skill_text: str, version: str, errors: list[str], warnings: list[str]) -> None:
    block = frontmatter(skill_text, errors)
    if not block:
        return
    keys = {match.group(1) for line in block.splitlines() if (match := TOP_LEVEL_FRONTMATTER_KEY.match(line))}
    unexpected = sorted(keys - ALLOWED_FRONTMATTER_KEYS)
    if unexpected:
        errors.append(f"unexpected SKILL.md frontmatter keys: {', '.join(unexpected)}")
    name = scalar_from_frontmatter(block, "name")
    description = scalar_from_frontmatter(block, "description")
    if name != "gauntlet-loop":
        errors.append("SKILL.md name must be gauntlet-loop")
    if not description:
        errors.append("SKILL.md description is required")
    elif len(description) > 1024 or "<" in description or ">" in description:
        errors.append("SKILL.md description violates Agent Skills length/character constraints")
    if metadata_version(block) != version:
        errors.append("SKILL.md metadata.version does not match VERSION")
    line_count = skill_text.count("\n") + 1
    if line_count > 500:
        warnings.append(f"SKILL.md is {line_count} lines; progressive-disclosure guidance recommends at most 500")


def validate_local_references(skill_text: str, errors: list[str]) -> None:
    for relative in sorted(set(LOCAL_SKILL_PATH.findall(skill_text))):
        if not (SKILL_DIR / relative).is_file() and not (SKILL_DIR / relative).is_dir():
            errors.append(f"SKILL.md references missing skill path: {relative}")


def validate_manifests(version: str, errors: list[str]) -> None:
    for relative_path, accessor in MANIFEST_VERSION_PATHS:
        parsed = load_json(relative_path, errors)
        if parsed is None:
            continue
        try:
            manifest_version = get_nested(parsed, accessor)
        except KeyError:
            errors.append(f"missing version field in {relative_path}")
            continue
        if manifest_version != version:
            errors.append(f"version mismatch in {relative_path}: {manifest_version!r} != {version!r}")

    for relative_path in (
        ".claude-plugin/plugin.json",
        ".codex-plugin/plugin.json",
    ):
        parsed = load_json(relative_path, errors)
        if isinstance(parsed, dict) and parsed.get("skills") != ["./skills/gauntlet-loop"]:
            errors.append(f"{relative_path} must expose only ./skills/gauntlet-loop")


def validate_schemas(errors: list[str]) -> None:
    for path in sorted((SKILL_DIR / "schemas").glob("*.schema.json")):
        relative = path.relative_to(ROOT).as_posix()
        parsed = load_json(relative, errors)
        if isinstance(parsed, dict) and parsed.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"{relative} must declare JSON Schema draft 2020-12")

def validate_evals(errors: list[str]) -> None:
    for relative in ("evals/activation-cases.json", "evals/bug-hunt-cases.json"):
        parsed = load_json(relative, errors)
        if not isinstance(parsed, dict):
            continue
        if parsed.get("schemaVersion") != "1.0":
            errors.append(f"{relative} must use schemaVersion 1.0")
        cases = parsed.get("cases")
        if not isinstance(cases, list) or not cases:
            errors.append(f"{relative} must contain a non-empty cases array")
            continue
        case_ids: list[str] = []
        for index, case in enumerate(cases):
            if not isinstance(case, dict):
                errors.append(f"{relative} case {index} must be an object")
                continue
            case_id = case.get("id")
            if not isinstance(case_id, str) or not case_id:
                errors.append(f"{relative} case {index} has no stable id")
            else:
                case_ids.append(case_id)
            if "expected" not in case:
                errors.append(f"{relative} case {case_id or index} has no expected result")
        if len(case_ids) != len(set(case_ids)):
            errors.append(f"{relative} contains duplicate case ids")



def scan_security(errors: list[str]) -> dict[str, object]:
    findings: list[dict[str, str]] = []
    files_scanned = 0
    for path in sorted(SKILL_DIR.rglob("*")):
        if path.is_symlink():
            errors.append(f"skill package may not contain symlinks: {path.relative_to(ROOT).as_posix()}")
            continue
        if not path.is_file():
            continue
        files_scanned += 1
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError:
            errors.append(f"skill package contains non-UTF-8 file: {path.relative_to(ROOT).as_posix()}")
            continue
        for rule, pattern in SECURITY_PATTERNS:
            if pattern.search(text):
                findings.append({"path": path.relative_to(ROOT).as_posix(), "rule": rule})
    if findings:
        errors.append(f"security policy scan found {len(findings)} possible secret material item(s)")
    return {
        "scanner": "gauntlet-loop-local-static-policy-v1",
        "scope": "skills/gauntlet-loop",
        "filesScanned": files_scanned,
        "status": "PASS" if not findings else "FAIL",
        "findings": findings,
        "limitations": "Static package policy checks only; this is not semantic safety or behavioral certification.",
    }


def clean_dist() -> None:
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for name in DIST_OUTPUTS:
        (DIST_DIR / name).unlink(missing_ok=True)


def package_skill() -> tuple[Path, list[str]]:
    archive_path = DIST_DIR / "gauntlet-loop.skill"
    members: list[str] = []
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in sorted(SKILL_DIR.rglob("*")):
            if not path.is_file() or path.is_symlink() or path.name == ".DS_Store" or "__pycache__" in path.parts:
                continue
            member = path.relative_to(SKILL_DIR.parent).as_posix()
            info = zipfile.ZipInfo(member, date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
            members.append(member)
    return archive_path, members


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def validate_and_package() -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    clean_dist()

    for relative in REQUIRED_PATHS:
        if not (ROOT / relative).is_file():
            errors.append(f"missing required path: {relative}")

    version = ""
    try:
        version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    except OSError as exc:
        errors.append(f"cannot read VERSION: {exc}")
    if not VERSION_PATTERN.fullmatch(version):
        errors.append(f"VERSION must be semantic x.y.z, got {version!r}")

    skill_text = ""
    try:
        skill_text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"cannot read SKILL.md: {exc}")
    if skill_text:
        validate_frontmatter(skill_text, version, errors, warnings)
        validate_local_references(skill_text, errors)

    validate_manifests(version, errors)
    validate_schemas(errors)
    validate_evals(errors)
    security = scan_security(errors)
    write_json(DIST_DIR / "security-scan.json", security)

    members: list[str] = []
    archive_path = DIST_DIR / "gauntlet-loop.skill"
    archive_hash = ""
    if not errors:
        archive_path, members = package_skill()
        archive_hash = sha256(archive_path)
        (DIST_DIR / "SHA256SUMS").write_text(
            f"{archive_hash}  {archive_path.name}\n", encoding="utf-8"
        )

    report_lines = [
        "Gauntlet Loop validation report",
        f"Version: {version or 'UNKNOWN'}",
        f"Result: {'PASS' if not errors else 'FAIL'}",
        f"Packaged files: {len(members)}",
        f"Warnings: {len(warnings)}",
        f"Errors: {len(errors)}",
    ]
    report_lines.extend(f"WARNING: {warning}" for warning in warnings)
    report_lines.extend(f"ERROR: {error}" for error in errors)
    (DIST_DIR / "VALIDATION_REPORT.txt").write_text("\n".join(report_lines) + "\n", encoding="utf-8")
    write_json(
        DIST_DIR / "RELEASE_STATUS.json",
        {
            "archive": archive_path.name if archive_path.exists() else None,
            "archiveSha256": archive_hash or None,
            "errors": errors,
            "packagedFiles": len(members),
            "ready": not errors,
            "version": version or None,
            "warnings": warnings,
        },
    )
    return errors, warnings


def main() -> int:
    errors, warnings = validate_and_package()
    print(f"Gauntlet Loop validation: {len(errors)} error(s), {len(warnings)} warning(s)")
    for error in errors:
        print(f"ERROR: {error}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
