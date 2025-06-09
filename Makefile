install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv testing.py

format:
	black *.py
