# Local validation record

Date: November 1, 2026 (America/New_York).

Environment: Windows authoring workspace; PowerShell 7 for PowerShell checks and Python 3.12 for Python checks. These are local test results, not a CI result or a completed production incident.

## Scope

Network and process behavior are mocked in the unit suite. A prior localhost-only smoke run resolved loopback addresses and recorded a failed TCP connection; no remote infrastructure was exercised.

## Observed output

```text
test_command_timeout (test_net_report.NetworkTests.test_command_timeout) ... ok
test_failed_probe (test_net_report.NetworkTests.test_failed_probe) ... ok
test_hosts (test_net_report.NetworkTests.test_hosts) ... ok
test_imported_function_validates_before_network (test_net_report.NetworkTests.test_imported_function_validates_before_network) ... ok
test_missing_tool (test_net_report.NetworkTests.test_missing_tool) ... ok
test_no_addresses_is_not_success (test_net_report.NetworkTests.test_no_addresses_is_not_success) ... ok
test_no_implicit_probes (test_net_report.NetworkTests.test_no_implicit_probes) ... ok
test_ports (test_net_report.NetworkTests.test_ports) ... ok
test_successful_probe (test_net_report.NetworkTests.test_successful_probe) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.276s

OK
```

## Reproduce

Run the test command in this repository's README. A passing suite establishes only the cases represented in the tests; add actual lab evidence before claiming end-to-end deployment or recovery.
