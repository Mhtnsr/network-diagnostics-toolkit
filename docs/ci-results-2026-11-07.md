# Hosted CI validation — November 7, 2026

**Observed result: all jobs passed.**

[Inspect the run](https://github.com/Mhtnsr/network-diagnostics-toolkit/actions/runs/42377633386) · tested source commit: `1583cad5f8cfb5fa6e84cb9ccd00ad079519bfd0`.

| Job | Result |
| --- | --- |
| Python 3.12 / windows-latest | success |
| Python 3.10 / ubuntu-latest | success |
| Python 3.10 / windows-latest | success |
| Python 3.12 / ubuntu-latest | success |

## Scope

The unit suite mocks network/process operations; it does not establish behavior on a customer network.

These are GitHub-hosted runner results. They are not evidence of a personal home-lab build, an employer deployment, or a resolved customer incident. Later runs can have different results; inspect the [workflow history](https://github.com/Mhtnsr/network-diagnostics-toolkit/actions/workflows/checks.yml) for current status.

## What changed during setup

The first PowerShell workflow definition failed validation because a matrix expression was not supported in the shell field. It was changed to two explicit runtime jobs; the linked run is the corrected passing result. The Python workflows passed their first runs.
