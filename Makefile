.PHONY: build dev run

build:
	@if ! command -v patchelf >/dev/null 2>&1; then \
		echo "Error: patchelf 未安装"; \
		if command -v dnf >/dev/null 2>&1; then \
			echo "运行: sudo dnf install patchelf"; \
		elif command -v yum >/dev/null 2>&1; then \
			echo "运行: sudo yum install patchelf"; \
		else \
			echo "运行: sudo apt install patchelf"; \
		fi; \
		exit 1; \
	fi
	@if [ ! -f /usr/include/Python.h ] && [ ! -f /usr/include/python3.14/Python.h ]; then \
		echo "Error: Python 开发头文件未安装"; \
		if command -v dnf >/dev/null 2>&1; then \
			echo "运行: sudo dnf install python3-devel"; \
		elif command -v yum >/dev/null 2>&1; then \
			echo "运行: sudo yum install python3-devel"; \
		else \
			echo "运行: sudo apt install python3-dev"; \
		fi; \
		exit 1; \
	fi
	nuitka --onefile main.py --output-filename=pt-auto-sign

dev:
	uv run python main.py

run: build
	./pt-auto-sign
