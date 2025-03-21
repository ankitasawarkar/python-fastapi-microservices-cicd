install:
	#install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	# Download SpaCy model
	python -m spacy download en_core_web_sm
format:
	#format code
	black *.py mylib/*py
lint: 
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*py
test:
	#test
	python -m pytest -vv --cov=mylib --cov=main test_*.py
build:
	#build container 
deploy:
	#deploy
all: install lint test deploy