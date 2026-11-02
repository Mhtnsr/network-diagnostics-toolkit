# Network Diagnostics Toolkit

Single-host DNS, ping, route, and TCP diagnostics with structured JSON reports.

**Owner:** [Mahamat Nassour Ahmat](https://github.com/Mhtnsr) · IT Support Specialist → Systems Administrator

## Problem

Ad hoc network checks are difficult to compare and hand off.

## Solution

Collect DNS results for one explicit host; optionally run ping, bounded route tracing, and up to eight TCP port checks. No network ranges or discovery scanning. JSON supports consistent incident notes.

## Usage

Run from the repository root. Use an isolated, authorized environment and inspect source before execution.

```bash
python scripts/net_report.py --host localhost
# Opt-in checks on your own local endpoint only:
python scripts/net_report.py --host localhost --ports 443 --probe --ping --route
python -m unittest discover -s tests -v
```

## Validation and limits

Mocked tests and a localhost-only smoke run validate selected paths. Windows/Linux command availability varies; DNS resolution has OS-controlled timeout behavior. TCP success is not an application health check. Reports may contain addresses and routes: keep them private until sanitized.

## Screenshots and evidence

[Evidence checklist](evidence/README.md). Placeholder: add a sanitized capture of the actual execution or lab result here after validation. No screenshots or outcomes are fabricated.

<!-- Example after creating the file: ![Sanitized lab result](evidence/lab-result.png) -->

## Repository map

Source belongs in `scripts/`, reproducible checks in `tests/`, synthetic inputs in `examples/`, design notes in `docs/`, reusable records in `templates/`, and sanitized proof in `evidence/`. Only directories relevant to this project are created.

## Next steps

- Capture a reproducible lab run with expected versus observed behavior.
- Document failure cases and recovery or escalation.
- Update validation status only after recording actual results.

## Security

See [SECURITY.md](SECURITY.md). No company data, credentials, internal topology, or live ticket details belong here.

## License

[MIT](LICENSE). A personal learning project; not affiliated with or endorsed by USEReady, Microsoft, CompTIA, or other vendors.
