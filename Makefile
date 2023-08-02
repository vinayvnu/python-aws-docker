install:
	# install files
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black *.py mylib/*.py

lint:
	# it disables Recommended warnings(R) and configuration warnings(C)
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib test_logic.py
