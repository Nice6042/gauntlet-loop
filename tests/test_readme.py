"""Regression tests for the repository's public landing-page journey."""

from __future__ import annotations

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"


def read_readme(test: unittest.TestCase) -> str:
    """Return the landing page after reporting a useful missing-file failure."""
    test.assertTrue(
        README.is_file(),
        "README.md is missing, so repository visitors have no project or install-status guidance",
    )
    return README.read_text(encoding="utf-8")


class ReadmeJourneyTests(unittest.TestCase):
    def test_landing_page_sets_safe_installation_expectations(self) -> None:
        text = read_readme(self)
        opening = text[:1200]

        self.assertRegex(
            opening.casefold(),
            r"installation is not currently available|not currently installable",
            "the unavailable installation status must be visible before visitors reach setup details",
        )
        self.assertIn("skills/gauntlet-loop/SKILL.md", opening)
        self.assertIn("No valid skills found", opening)
        self.assertNotIn(
            "npx ",
            text.casefold(),
            "dead installation commands must not be offered while the canonical skill is absent",
        )

        for route in ("Agent Skills CLI", "Codex plugin", "Claude Code plugin"):
            with self.subTest(route=route):
                self.assertIn(route, text)

        self.assertIn(
            "commands are intentionally withheld",
            text.casefold(),
            "planned routes need an explicit explanation for the missing commands",
        )

    def test_landing_page_has_an_accessible_markdown_outline(self) -> None:
        text = read_readme(self)
        headings = [
            (len(match.group(1)), match.group(2).strip())
            for match in re.finditer(r"^(#{1,6})\s+(.+?)\s*$", text, re.MULTILINE)
        ]

        self.assertTrue(headings, "README.md needs a visible title")
        self.assertEqual(1, headings[0][0], "the first heading must be the page title")
        self.assertEqual(
            1,
            sum(level == 1 for level, _ in headings),
            "README.md must have exactly one level-one heading",
        )
        self.assertEqual(
            len(headings),
            len({title.casefold() for _, title in headings}),
            "heading labels must be unique for clear screen-reader navigation",
        )

        for previous, current in zip(headings, headings[1:]):
            self.assertLessEqual(
                current[0],
                previous[0] + 1,
                f"heading level jumps from {previous[1]!r} to {current[1]!r}",
            )

        for label, _target in re.findall(r"(?<!!)\[([^]]+)\]\(([^)]+)\)", text):
            with self.subTest(link_label=label):
                self.assertNotIn(
                    label.strip().casefold(),
                    {"here", "click here", "link", "more"},
                    "link labels must describe their destination out of context",
                )


if __name__ == "__main__":
    unittest.main()
