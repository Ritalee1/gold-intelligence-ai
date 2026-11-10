# Gold Intelligence AI

**An AI-powered, multi-asset market intelligence and trading analytics platform.**

Gold Intelligence AI is an evolving software engineering project exploring the integration of artificial intelligence, financial market analysis, technical indicators, and automated research workflows.

The initial development focus is XAUUSD (Gold), with an extensible architecture designed to support additional financial instruments.

## Project Vision

To develop an intelligent market research environment that combines quantitative analysis, interactive financial visualisation, AI-assisted research, and trading performance analytics.

## Planned Features

- Multi-asset market data analysis
- Interactive candlestick charts and market visualisation
- Technical indicators and market trend analysis
- AI-assisted market research
- Historical strategy backtesting
- Trading journal and performance analytics
- Risk management and position sizing tools
- Agentic AI research and reporting workflows

## Technology Stack

- Python
- Pandas and NumPy
- Streamlit
- Plotly
- SQL
- Scikit-learn
- Claude Code

## Architecture

A `src/`-layout Python package. Dependencies point one way: the UI, CLI and agents call services; services use the domain and data layers; the domain layer has no I/O.

```
src/gold_intel/
├── core/        # Domain models: instruments, bars, timeframes, trades, signals
├── data/        # Market data providers, validation, storage (Parquet + DuckDB)
├── features/    # Technical indicators and feature engineering (no lookahead)
├── backtest/    # Backtesting engine, cost model, performance metrics
├── risk/        # Position sizing, exposure and drawdown controls
├── journal/     # Trade journal, broker imports, performance analytics
├── ml/          # ML pipelines, time-series cross-validation, experiment tracking
├── agents/      # LLM research agents (read-only; never place trades)
├── config.py    # Settings from environment / .env
└── cli.py       # `gold-intel` command-line interface
```

Instrument-specific details (tick size, contract size, sessions) live in an instrument registry rather than in code, so new asset classes can be added without rewriting the analytics.

## Getting Started

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
uv sync                      # create .venv and install dependencies
cp .env.example .env         # optional: add API keys (never commit .env)
uv run gold-intel --version
uv run gold-intel info       # show active configuration
```

## Development

```bash
uv run ruff check .          # lint
uv run ruff format .         # format
uv run mypy                  # strict type checking
uv run pytest --cov          # tests with coverage
uv run pre-commit install    # run lint/format hooks on every commit
```

CI (GitHub Actions) runs lint, format check, mypy and tests on Ubuntu and Windows for Python 3.12 and 3.13.

## Roadmap

| Milestone | Scope | Status |
|---|---|---|
| M0 | Project skeleton, tooling, CI | Done |
| M1 | Data layer: providers, validation, Parquet storage, `ingest` CLI | Planned |
| M2 | Technical indicators | Planned |
| M3 | Streamlit dashboard | Planned |
| M4 | Backtesting engine and metrics (MVP complete) | Planned |
| M5 | Risk management and trading journal | Planned |
| M6 | Machine learning with walk-forward validation | Planned |
| M7 | Agentic AI research reports | Planned |
| M8 | Multi-asset expansion (Forex, stocks, crypto) | Planned |

## Development Status

**Status: Milestone 0 complete (project foundation)**

Features are implemented incrementally, with each milestone tested and documented before the next begins.

## Project Goals

- Apply AI engineering principles to financial market research.
- Develop practical agentic AI workflows.
- Strengthen Python, data engineering, and software development skills.
- Build an extensible and maintainable application architecture.

---

*An independent AI engineering and financial analytics project.*
