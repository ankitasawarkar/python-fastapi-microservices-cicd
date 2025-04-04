# python-fastapi-microservices-cicd

[![Python application test with Github Actions](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml/badge.svg)](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml)

![Python application test with Github Actions](https://codebuild.us-east-2.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiY2RXa0RRUy9TbmtpSG50V3J6TldIdzU3alZlMlpTZFc5eEMzTFAwaXR6ZmVmU2s1b2liQ0JuWEdSdys5S1g4cnZZYUpnMmNMYnljeHRyM1g3a0pvYlhnPSIsIml2UGFyYW1ldGVyU3BlYyI6Ikx2WGxsN0xlZVpvVm5XR2IiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

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
        1. Makefile Commands: The `Makefile` includes commonly used commands to streamline project setup, testing, and deployment. Usage: Run the commands using:
            ```bash
            make <target>
            ```
        2.  To add the lifecycle of the project `make install`, `make deploy` we can see all commands of `make all` will give #install commands #flake8 or #pylint #test #deploy\

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
        Change in .github/devops.yml as `make <target>` then commit and push code. After that CI/CD pipeline process start build automatically. Same follows to other steps as well. <target> = [install, format, lint, test, build, run, deploy, all]
    ```
    git add .github
    git add *
    git commit -m "lint process check"
    git push
    ```  
4. **Source**
    1. Build **cli** to code converts the wiki function into a CLI tool to make it user-friendly and can test on the terminal using **Python Fire library** `./cli-fire.py --help` to test logic.
    ```bash
    touch cli-fire.py
    chmod +x cli-fire.py
    ./cli-fire.py --help
    ```
    Test function:\
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
    1. ***AWS***
        1. **ECR**
            
            Amazon ECR >> Create Repositories >> <ins>my_first_container_wiki</ins>
            
            `View Push Command` copies all commands into the Makefile build section.

        2. Continous Integration using **CodeBuild**
        
           Developer Tools >> CodeBuild >> Create Build projects >> <ins>Deploy-python-microservice-cicd</ins>

     		buildspec.yml file added
     		
     		<img src="images/1.1.png" width="400" />
            <img src="images/1.2.png" width="400" />
            <img src="images/1.3.png" width="400" />
            <img src="images/1.4.png" width="400" />
            <img src="images/1.5.png" width="400" />
            
            ERROR:-            
            <img src="images/1.6.png" width="400" />
            
            Solution:-
            <img src="images/1.7.png" width="400" />
     		
     	3. After Continous Delivery its time to proceed for Paas for **Continous Deploy** using **ECS, ECR and, App Runner** 
     	     <img src="images/2.1.png" width="400" />
            <img src="images/2.2.png" width="400" />
            <img src="images/2.3.png" width="400" />
            
            Finally able to access project: https://xsb3usqq7s.us-east-2.awsapprunner.com/docs
            
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

## Reference

* [Getting Started with AWS - Create Continuous Delivery Pipeline](https://aws.amazon.com/getting-started/hands-on/create-continuous-delivery-pipeline/)
* [AWS- Connect GitHub using OAuth (console)](https://docs.aws.amazon.com/codebuild/latest/userguide/oauth-app-github.html)
