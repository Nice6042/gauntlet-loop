from __future__ import annotations

import hashlib
import json
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
            "gauntlet-loop/references/delivery-protocol.md",
            "gauntlet-loop/templates/delivery-task.md",
            "gauntlet-loop/templates/delivery-campaign-state.md",
            "gauntlet-loop/templates/delivery-main-agent-prompt.md",
            "gauntlet-loop/templates/builder-prompt.md",
            "gauntlet-loop/templates/comparison-prompt.md",
            "gauntlet-loop/templates/critic-prompt.md",
            "gauntlet-loop/templates/delivery-integration-roles.md",
            "gauntlet-loop/schemas/delivery-task.schema.json",
            "gauntlet-loop/schemas/delivery-campaign.schema.json",
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

    def test_delivery_task_covers_all_universal_metrics(self) -> None:
        schema = json.loads(
            (ROOT / "skills" / "gauntlet-loop" / "schemas" / "delivery-task.schema.json").read_text(
                encoding="utf-8"
            )
        )
        required_metrics = set(schema["properties"]["metrics"]["required"])
        self.assertEqual(
            {
                "requirements_fidelity",
                "functional_correctness",
                "hidden_edge_cases",
                "regression_risk",
                "code_quality",
                "architecture",
                "maintainability",
                "extensibility",
                "scalability",
                "performance",
                "security",
                "privacy",
                "error_handling",
                "reliability",
                "test_quality_and_coverage",
                "visual_quality",
                "ux_consistency",
                "accessibility",
                "asset_quality",
                "originality_and_licensing",
                "platform_compatibility",
                "deployment_readiness",
                "documentation",
                "comparison_against_supplied_references",
                "future_proofness",
                "integration_readiness",
            },
            required_metrics,
        )

    def test_delivery_task_schema_carries_review_and_comparison_gates(self) -> None:
        schema = json.loads(
            (ROOT / "skills" / "gauntlet-loop" / "schemas" / "delivery-task.schema.json").read_text(
                encoding="utf-8"
            )
        )
        self.assertIn("closurePolicy", schema["required"])
        self.assertIn("reviews", schema["properties"])
        self.assertNotIn("reviews", schema["required"])
        self.assertIn("independentComparator", schema["properties"]["roleRouting"]["required"])
        comparison_required = schema["properties"]["comparisons"]["items"]["required"]
        self.assertIn("parityReceipt", comparison_required)
        self.assertIn("comparatorReportArtifactId", comparison_required)
        self.assertIn("labelMappingArtifactId", comparison_required)
        self.assertIn("allOf", schema)

    def test_delivery_campaign_schema_carries_terminal_gates(self) -> None:
        schema = json.loads(
            (
                ROOT
                / "skills"
                / "gauntlet-loop"
                / "schemas"
                / "delivery-campaign.schema.json"
            ).read_text(encoding="utf-8")
        )
        self.assertTrue({"activeScheduler", "findings", "rulings", "finalGate"}.issubset(schema["required"]))
        final_required = set(schema["properties"]["finalGate"]["required"])
        self.assertTrue(
            {
                "persistentFinalReportArtifactId",
                "persistentFinalVerdict",
                "blindReportArtifactId",
                "blindVerdict",
                "mainVerificationReceiptId",
                "deferredMetricsReconciled",
                "openHardFindings",
            }.issubset(final_required)
        )
        self.assertIn("allOf", schema)

    def test_both_campaign_schemas_constrain_concurrency_targets(self) -> None:
        schema_dir = ROOT / "skills" / "gauntlet-loop" / "schemas"
        for name in ("delivery-campaign.schema.json", "bug-campaign.schema.json"):
            schema = json.loads((schema_dir / name).read_text(encoding="utf-8"))
            concurrency = schema["properties"]["concurrency"]
            self.assertIn("allOf", concurrency)
            serialized = json.dumps(concurrency["allOf"], sort_keys=True)
            self.assertIn("SUSTAINED", serialized)
            self.assertIn('"minimum": 1', serialized)


if __name__ == "__main__":
    unittest.main()
