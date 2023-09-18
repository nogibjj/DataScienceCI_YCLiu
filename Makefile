install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py #--cov=main --cov=mylib
	python -m pytest --nbval main.ipynb

format:	
	black *.py 

lint:
	#pylint --disable=R,C --ignore-patterns=test_.*?py *.py #mylib/*.py
	ruff check *.py #mylib/*.py
	
#container-lint:
	#docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

#deploy:
	#deploy goes here
		
all: install lint test format deploy