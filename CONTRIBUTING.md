# Contributing

## Getting set up

```bash
git clone https://github.com/Speed-boo3/grc-project.git
cd grc-project
pip install -r requirements.txt
```

## Running the tests

```bash
pytest tests/
```

All tests should pass before opening a pull request.

## Adding a new risk

Risks live in `grc/risk-assessment/sample_risks.json`. Each risk needs an ID, name, likelihood (1-5), impact (1-5), owner and treatment.

## Reporting a bug

Open an issue and describe what happened, what you expected, and how to reproduce it.
