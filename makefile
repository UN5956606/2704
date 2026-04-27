.PHONY: test

setup:
	uv sync

test:
	PYTHONPATH=. uv run pytest