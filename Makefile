install:
	pip install --upgrade pip && \
		pip install -r requirements.txt

test:
	python -m pytest -vv test_Exam.py

format:
	black *.py
