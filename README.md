# Gauntlet Loop

> **Publication status: installation is not currently available.**
>
> The default branch does not yet contain the canonical
> `skills/gauntlet-loop/SKILL.md` payload. A live Agent Skills discovery attempt
> currently ends with `No valid skills found`. Do not attempt installation until
> every item in [Installation readiness](#installation-readiness) is satisfied.

The public tree currently contains release bootstrap and certification
workflows, but no installable skill. This page documents that state without
presenting dead setup commands as usable instructions.

## What is available today

- Release bootstrap and certification workflows are present on the default
  branch.
- The runnable skill payload, plugin manifests, version file, license, and
  release artifacts are absent.
- The [GitHub Releases page](https://github.com/Nice6042/gauntlet-loop/releases)
  does not yet contain an installable release.
- This README is a status and discovery page; its presence is not evidence that
  the skill is ready to install.

## Installation readiness

Treat installation as available only after all of these conditions are true:

1. `skills/gauntlet-loop/SKILL.md` exists on the default branch and includes the
   canonical `gauntlet-loop` name and description metadata.
2. The Codex, Claude Code, and Agent marketplace manifests are present in the
   repository.
3. `VERSION` and `LICENSE` are present.
4. The [GitHub Releases page](https://github.com/Nice6042/gauntlet-loop/releases)
   lists a non-draft release bound to the published source.
5. The relevant certification run is successful in the
   [GitHub Actions history](https://github.com/Nice6042/gauntlet-loop/actions).

If any item is missing, the repository is still a publication bootstrap rather
than an installable Gauntlet Loop distribution.

## Planned installation routes

Installation commands are intentionally withheld while the canonical skill and
host manifests are absent. Publishing commands before those files exist would
send users through a setup flow that cannot succeed.

### Agent Skills CLI

The repository is intended to expose one discoverable skill named
`gauntlet-loop` through the Agent Skills CLI after publication.

### Codex plugin

A Codex marketplace manifest is planned so the same canonical skill can be
installed as a Codex plugin after publication.

### Claude Code plugin

A Claude Code marketplace manifest is planned so the same canonical skill can
be installed as a Claude Code plugin after publication.

## Troubleshooting

### Agent tooling reports “No valid skills found”

For the current public tree, this message follows from the absent
`skills/gauntlet-loop/SKILL.md` payload. Repeatedly running an installation
command will not publish that file. Recheck the readiness conditions instead.

### The repository has no release

The empty Releases page means no GitHub release or attached release artifact is
currently available. Git tags and GitHub Releases are separate signals; use the
[GitHub Releases page](https://github.com/Nice6042/gauntlet-loop/releases) for
the release-readiness check rather than inferring availability from another
location.

### A readiness item looks stale

Open a report in the
[Gauntlet Loop issue tracker](https://github.com/Nice6042/gauntlet-loop/issues)
and name the readiness item that disagrees with the public repository state.

## Maintainer hand-off

When the source is published, replace the unavailable status before adding any
installation command. Verify each command from a clean environment, record the
successful routes, and update `tests/test_readme.py` so the landing-page contract
matches the now-installable repository.
