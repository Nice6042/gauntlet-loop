from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github" / "workflows"
PINNED_SOURCE_SHA256 = (
    "d56ea5695dc579b9c9167a0862a101caf1e19afd83b3cb1686188b10f0e4a123"
)
EXTERNAL_SOURCE_WORKFLOWS = (
    "final-install-proof.yml",
    "finalize-source-release.yml",
    "publish-gauntlet-loop.yml",
)


class ReleaseSourceTrustTests(unittest.TestCase):
    def test_external_source_uses_repository_pinned_digest(self) -> None:
        for name in EXTERNAL_SOURCE_WORKFLOWS:
            workflow = (WORKFLOW_DIR / name).read_text(encoding="utf-8")
            with self.subTest(workflow=name):
                self.assertIn(
                    f"SOURCE_SHA256: {PINNED_SOURCE_SHA256}",
                    workflow,
                    "the release source must be bound to the repository-pinned digest",
                )
                self.assertNotIn(
                    "SOURCE_SHA_URL",
                    workflow,
                    "a checksum from the archive host is not an authenticity proof",
                )

    def test_digest_is_checked_before_remote_archive_extraction(self) -> None:
        for name in EXTERNAL_SOURCE_WORKFLOWS:
            workflow = (WORKFLOW_DIR / name).read_text(encoding="utf-8")
            with self.subTest(workflow=name):
                download = workflow.index('"$SOURCE_URL"')
                verify = workflow.index("sha256sum --check --strict", download)
                extraction_offsets = [
                    workflow.find(command, verify)
                    for command in (
                        'tar -xzf "$archive"',
                        'tar -xzf "$SOURCE_ARCHIVE"',
                    )
                ]
                extraction_offsets = [
                    offset for offset in extraction_offsets if offset >= 0
                ]
                self.assertTrue(extraction_offsets, "remote archive is never extracted")
                self.assertLess(download, verify)
                self.assertLess(verify, min(extraction_offsets))


if __name__ == "__main__":
    unittest.main()
