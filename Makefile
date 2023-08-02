install:
	# install files
	pip install --upgrade pip
	pip install -r requirements.txt

format:
	black *.py mylib/*.py