# Contributing

Small, reproducible improvements are welcome: tests, clearer report interpretation, and documented cross-platform behavior.

## Run the checks

Use Python 3.10 or newer; no third-party packages are required.

```bash
python -m unittest discover -s tests -v
```

Open a branch and a pull request describing the problem, the change, the command you ran, and its result. Identify your operating system and Python version. Keep example data synthetic; do not attach reports from customer or employer systems.

## Starter task: real loopback TCP coverage

The current TCP success and failure unit tests mock `socket.create_connection`. Add a separate integration test file, `tests/test_loopback.py`, to exercise the actual socket path without contacting another machine.

Acceptance criteria:

- Bind a standard-library TCP listening socket to `127.0.0.1` on port `0`, then obtain the assigned port with `getsockname()`.
- Call `collect('127.0.0.1', [port], probe=True)` and assert that the matching TCP result is `connected`.
- Keep the listener alive until collection returns, then close it reliably with a context manager. One connection fits in the listen backlog, so an accepting thread is unnecessary.
- For a refused-connection test, reserve a separate loopback socket without calling `listen()` and keep it bound while probing. Avoid closing a socket and assuming its old port remains unused.
- Do not require administrator rights, fixed ports, internet access, DNS changes, firewall changes, or third-party dependencies.
- Keep ping and route disabled. Use literal IPv4 loopback so the test does not depend on the machine's `localhost` address-family ordering.
- Run the existing suite plus the new tests. Confirm the existing Windows/Linux and Python 3.10/3.12 CI matrix passes before merging.

These tests demonstrate local TCP connection behavior only; they do not validate routing, TLS, authentication, or remote service health. If a platform prevents local binding, report the actual error rather than hiding every failure with an unconditional skip.

## Collaboration and credit

Separate independent PRs from genuinely joint work. Use Git's `Co-authored-by` trailer only when another person materially helped author that change, with their consent and their preferred GitHub-associated email. Review alone does not imply coauthorship. Do not publish anyone's email without consent.

Changes remain subject to review and the repository's MIT license. See [SECURITY.md](SECURITY.md) for reporting security concerns.
