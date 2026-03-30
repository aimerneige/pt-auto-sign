.PHONY: build dev run

build:
	nuitka --onefile main.py --output-filename=pt-auto-sign

dev:
	uv run python main.py

run: build
	./pt-auto-sign
