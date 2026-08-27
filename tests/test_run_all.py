from __future__ import annotations

import hashlib
import sys
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import run_all  # noqa: E402


class ValidationAndPackagingTests(unittest.TestCase):
    def test_repository_contract_passes(self) -> None:
        errors, _warnings = run_all.validate_and_package()
        self.assertEqual([], errors)

    def test_package_is_deterministic_and_complete(self) -> None:
        first_errors, _ = run_all.validate_and_package()
        self.assertEqual([], first_errors)
        archive = ROOT / "dist" / "gauntlet-loop.skill"
        first_hash = hashlib.sha256(archive.read_bytes()).hexdigest()

        second_errors, _ = run_all.validate_and_package()
        self.assertEqual([], second_errors)
        second_hash = hashlib.sha256(archive.read_bytes()).hexdigest()
        self.assertEqual(first_hash, second_hash)

        with zipfile.ZipFile(archive) as package:
            members = set(package.namelist())
        expected_members = {
            "gauntlet-loop/SKILL.md",
            "gauntlet-loop/references/bug-hunt-protocol.md",
            "gauntlet-loop/references/concurrency.md",
            "gauntlet-loop/references/output-quality.md",
            "gauntlet-loop/templates/main-agent-prompt.md",
            "gauntlet-loop/templates/finder-prompt.md",
            "gauntlet-loop/templates/spec-verifier-prompt.md",
            "gauntlet-loop/templates/fixer-prompt.md",
            "gauntlet-loop/templates/fix-verifier-prompt.md",
            "gauntlet-loop/templates/integration-roles.md",
            "gauntlet-loop/templates/bug-spec.md",
            "gauntlet-loop/templates/bug-campaign-state.md",
            "gauntlet-loop/schemas/bug-spec.schema.json",
            "gauntlet-loop/schemas/bug-campaign.schema.json",
        }
        self.assertTrue(expected_members.issubset(members))
        self.assertTrue(all(not name.startswith("/") and ".." not in Path(name).parts for name in members))

    def test_frontmatter_rejects_wrong_product_version(self) -> None:
        skill_text = (ROOT / "skills" / "gauntlet-loop" / "SKILL.md").read_text(encoding="utf-8")
        errors: list[str] = []
        warnings: list[str] = []
        run_all.validate_frontmatter(skill_text, "9.9.9", errors, warnings)
        self.assertIn("SKILL.md metadata.version does not match VERSION", errors)


if __name__ == "__main__":
    unittest.main()
