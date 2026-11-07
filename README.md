# Single-host network diagnostics

A Python utility for gathering a consistent network troubleshooting report for one explicit, authorized host.

## Checks

| Check | Default | What a result establishes |
| --- | --- | --- |
| OS DNS resolver | On | Whether the supplied name resolves through this machine's resolver |
| TCP connection | `--probe` | Whether a connection can be established to a selected port |
| Ping | `--ping` | Observed ICMP response behavior; lack of response alone does not prove an outage |
| Route trace | `--route` | A bounded view of responding hops; not a complete topology |

There is no network-range input or discovery scan. TCP input is limited to eight ports. The same host and port validation runs for CLI and imported-function use.

## Use

Python 3.10+ with the standard library. Ping/route checks also require the platform's command-line utilities. From the repository root:

```bash
python scripts/net_report.py --host localhost
python scripts/net_report.py --host localhost --ports 443 --probe
python scripts/net_report.py --host localhost --ping --route
python -m unittest discover -s tests -v
```

Output is JSON on stdout. There is no automatic upload. Review reports locally: DNS answers and route output can reveal private infrastructure.

## Implementation decisions

- No shell interpolation: subprocess commands receive argument lists.
- TCP connects have a three-second timeout; ping and route commands have process deadlines.
- Name resolution uses `getaddrinfo`; its wait time is controlled by the OS resolver and is not bounded by the TCP timeout.
- Missing utilities and command timeouts have explicit statuses.
- A completed command may have a non-zero return code. A TCP connection does not verify TLS, authentication, or application health.

## Validation and remaining work

[Validation record](docs/validation.md): fixture/mocked tests and a localhost-only smoke run. Route behavior across Windows/Linux and real network fault diagnosis are not yet lab-validated. No customer or employer network was tested.

[Evidence index](evidence/README.md) · [MIT license](LICENSE) · [Security](SECURITY.md)

## Automated checks

[CI configuration and limits](docs/ci.md) · [Latest workflow runs](https://github.com/Mhtnsr/network-diagnostics-toolkit/actions/workflows/checks.yml)
