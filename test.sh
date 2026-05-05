#!/bin/bash

set -uo pipefail

# Activate venv if needed
if [[ -z "${VIRTUAL_ENV:-}" ]]; then
	echo "Activating virtual env..."
	source venv/bin/activate
fi

if [[ -z "${VIRTUAL_ENV}" ]]; then
	echo "*** Not in virtual env."
	return 1
fi

echo "Unit tests…"
python -m unittest discover --quiet -s tests -p "*_test.py"
#pip show pytest --quiet && pytest --quiet --no-header --no-summary
echo "Code Lint…"
flake8 flextable/ tests/
