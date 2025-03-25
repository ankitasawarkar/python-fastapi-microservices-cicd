# python-fastapi-microservices-cicd

[![Python application test with Github Actions](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml/badge.svg)](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml)

### Code plan


1. **Make file:**
    1. **virtual env** \
        `python3 -m venv ~/.venv` or `virtualenv ~/.venv`

        `virtualenv ~/.venv`\
        `vim ~/.bashrc` \
        Sourcing python virtual environment\
        `source ~/.venv/bin/activate`\
            OR\
    
        `python -m venv venv`\
        `dir venv`\
        for bin folder\
        `source venv/bin/activate`\
        for Scripts folder\
        `venv/Scripts/activate`\
        checking for source code directory\
        `which python` --> /workspaces/python-fastapi-microservices-cicd/venv/bin/python
    
    2. **Requirement, Dockerfile & Makefile**
    
        `touch requirements.txt`\
        `touch Dockerfile`\
        `touch Makefile`
        1. Makefile Commands : The `Makefile` includes commonly used commands to streamline project setup, testing, and deployment. Usage: Run the commands using:
            ```bash
            make <target>
            ```
        2.  To add lifecycle of project `make install`, `make deploy` we can see all command of `make all` will give #install commands #flake8 or #pylint #test #deploy\

    3. **for logic and main start file**
        `mkdir mylib`\
        `touch mylib/__init__.py`\
        `touch mylib/logic.py`\
        `touch main.py`\

2. **requirement.txt**
    
    **Library Explanation & Usage for project:** 📌 These libraries help with data fetching, testing, linting, formatting, and building CLI tools efficiently. Freeze the lib vesions `pip freeze | less` and note it to file.

    **wikipedia**: A Python library to fetch and parse data from Wikipedia.
    ```python
    import wikipedia  
    print(wikipedia.summary("Python (programming language)"))  
    ```
    **pytest**: A testing framework for Python, used to write and run tests.
    ```bash
    pytest test_file.py  
    ```
    **pytest-cov**: A plugin for pytest to measure test coverage.
    ```bash
    pytest --cov=your_package  
    ```
    **pylint**: A static code analysis tool to check for errors and enforce style consistency, and detect issues that could lead to problems and coding standards. 
    ```bash
    pylint your_script.py  
    ```
    **black**: A code formatter that enforces consistent style.
    ```bash
    black your_script.py  
    ```
    **fire**: A library for auto-generating CLI interfaces from Python functions and classes.
    ```python
    import fire  
    
    def greet(name="World"):  
        print(f"Hello, {name}!")  
    
    if __name__ == '__main__':  
        fire.Fire(greet)  
    ```
    ```bash
    python script.py --name=Ankita  
    ```
4. **Makefile steps**\
        Change in .github/devops.yml as `make <target>` then commit and push code. After that CI/CD pipeline process start build automatically. Same follow to other steps as well.
    ```
    git add .github
    git add *
    git commit -m "lint process check"
    git push
    ```
    **a. install**\
        ```
        pip install --upgrade pip &&\
    	pip install -r requirements.txt
    	```\
        
    \
    \
    **b. format**\
    `black *.py mylib/*py`
    \
    \
    **c. lint**\
    `pylint --disable=R,C *.py mylib/*py`
    \
    \
    **d. test**\
    `python -m pytest -vv --cov=mylib test_logic.py`
    \
    \
    **e. build:**\
	#build container 
	\
    \
    **f. deploy:**\
	#deploy
	\
    \
    **g. all: install lint test deploy**
   
4. **Source**
    1. Build **cli** to code converts the wiki function into a CLI tool to make it user friendly and can test on terminal using **Python Fire library** `./cli-fire.py --help` to test logic.
    ```bash
    touch cli-fire.py
    chmod +x cli-fire.py
    ./cli-fire.py --help
    ```
    Test function:

    `./cli-fire.py --name "Deep_Learning"` --response-->> Deep learning is a subset of machine learning that focuses on utilizing neural networks to perform tasks such as classification, regression, and representation learning.\
    `./cli-fire.py search_wiki "Ankita"`

    2. FastAPI 
        check all APIs using <url>/docs for swagger docs look 
5. test
    ```bash
    # git Commands
    history
    
    
    ```
6. Docker file
   **Docker commands:**\
    `docker build -t <image-name> .` - latest or :v1 version & . indicate current directory\
    `docker image ls` - List of images \
    Run image with port:\
    `docker run -d -p 8000:8000 <image-name>`\
    `docker ps` - Check running ports\
    `docker logs <container-id>` - Check the logs\
    `docker stop $(docker ps -q)` - Stop all running containers\
    `docker rmi <inage-id>`\
    `docker rmi $(docker images -q)` - Remove all containers\
    `docker system prune -a --volumes -f` - Force Remove All Images (Even Dangling or Intermediate Layers)\
    
7. Infrastructure as code (IAC)
8. NLP module Explanation:
    Library:
    1. **spaCy:**
Used for tokenization, lemmatization, and removing stop words and punctuation. Lemmatization reduces words to their base form (e.g., "running" becomes "run").
    2. **TF-IDF:**
Calculates the importance of words in a document relative to a collection of documents. Words that appear frequently in a document but rarely in others are given higher importance. Adjust the TfidfVectorizer parameters (e.g., ngram_range, max_df, min_df) to see how they affect the results.
    3. **Cosine Similarity:**
Measures the similarity between two vectors (in this case, TF-IDF vectors) by calculating the cosine of the angle between them. A higher cosine similarity score indicates greater similarity.

    **`find_similar_documents` function:**\
    Takes a query, the TF-IDF matrix, the original documents, and the vectorizer as input. It then transforms the query into a TF-IDF vector, calculates the cosine similarity with all documents, and returns the most similar documents along with their similarity scores.
    
    **Apply to a real-world problem:**
    
    Consider using this project as a starting point for a real-world problem, such as document retrieval, topic modeling, or text summarization.

