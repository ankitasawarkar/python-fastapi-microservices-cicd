# python-fastapi-microservices-cicd

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
        --> to add lifecycle of project `make install`, `make deploy` we can see all command of `make all` will give #install commands #flake8 or #pylint #test #deploy

    `mkdir mylib`\
    `touch mylib/__init__.py`\
    `touch mylib/logic.py`\
    `touch main.py`\

3. source
4. test
5. Docker file
6. Infrastructure as code (IAC)
