# python-fastapi-microservices-cicd

[![Python application test with Github Actions](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml/badge.svg)](https://github.com/ankitasawarkar/python-fastapi-microservices-cicd/actions/workflows/devops.yml)

### Code plan

1. Make file - virtual env `python3 -m venv ~/.venv` or `virtualenv ~/.venv`

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

2. requirement.txt

    `touch requirements.txt`\
    `touch Dockerfile`\
    `touch Makefile`\
        --> Makefile Commands : The `Makefile` includes commonly used commands to streamline project setup, testing, and deployment. Usage: Run the commands using:
        ```bash
        make <target>
        ```
        --> to add lifecycle of project `make install`, `make deploy` we can see all command of `make all` will give #install commands #flake8 or #pylint #test #deploy\

 
    `mkdir mylib`\
    `touch mylib/__init__.py`\
    `touch mylib/logic.py`\
    `touch main.py`\

3.  Library Explanation & Usage: 📌 These libraries help with data fetching, testing, linting, formatting, and building CLI tools efficiently. Freeze the lib vesions `pip freeze | less` and note it to file.

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

4. source
5. test
6. Docker file
7. Infrastructure as code (IAC)

