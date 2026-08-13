    # J1939 CAN Bench Reader

    Independent public portfolio project for **Python**, **automation**,
    **systems integration** and **solutions engineering**.

    This repository was created from scratch with a fictional domain and
    synthetic data. It does not contain corporate code, real data, private
    endpoints, credentials, logs or proprietary rules.

    ## Problem

    CAN bench work needs safe examples for frame reading, parsing and serial output.

    ## Objective

    Demonstrate generic CAN/J1939 parsing and bench documentation with fictional frames.

    ## Current Features

    - Synthetic CAN frames.
- Generic CAN ID parser.
- Arduino serial demo.
- Bench documentation foundation.

    ## Architecture

    ```mermaid
    flowchart LR
        A["Synthetic input"] --> B["Python processing"]
        B --> C["Rules / validation"]
        C --> D["Generated local output"]
        D --> E["Future API / dashboard"]
    ```

    See [docs/architecture.md](docs/architecture.md) for details.

    ## Stack

    Current:

    `Python` `Arduino` `CAN` `J1939 concepts` `Synthetic frames`

    Planned evolution:

    - MCP2515
- Hardware bench tests
- PyTest
- Docs
- CI

    ## Run Locally

    ```powershell
    python examples/run_demo.py
    ```

    The demo uses only files under `data/sample/` and writes generated output
    to ignored local folders.

    ## Repository Workflow

    This project is intended to evolve through:

    - Issues for planned work.
    - Milestones for learning phases.
    - Small branches and pull requests.
    - Releases when a useful increment is ready.

    Draft issues are documented in [docs/github-issues.md](docs/github-issues.md).

    ## Roadmap

    See [ROADMAP.md](ROADMAP.md).

    ## Security and Independence

    See [SECURITY.md](SECURITY.md) and [DISCLAIMER.md](DISCLAIMER.md).
