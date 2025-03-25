install:
	#install commands
	pip install --upgrade pip &&\
	pip install -r requirements.txt
	# Download SpaCy model
	python -m textblob.download_corpora
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
	docker build -t deploy-fastapi .
run:
	#run docker
	#docker run -p 127.0.0.1:8080:8080 4dd8706b44d9
	docker run -p 8080:8080 deploy-fastapi
deploy:
	#deploy
	aws ecr get-login-password --region us-east-2 | docker login --username AWS --password-stdin 210226313522.dkr.ecr.us-east-2.amazonaws.com
	docker build -t my_first_container_wiki .
	docker tag my_first_container_wiki:latest 210226313522.dkr.ecr.us-east-2.amazonaws.com/my_first_container_wiki:latest
	docker push 210226313522.dkr.ecr.us-east-2.amazonaws.com/my_first_container_wiki:latest
all: install lint test deploy