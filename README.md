# Ventura

## Requirements

- `python` ^3.6
- `pip`
- `virtualenv` (_just `pip install virtualenv` if don't have_)
- `Docker`
- `NodeJS for npm`

## Installation'

Instructions for how to download/install the code onto your machine.

### Create Virtual Environment

The following command creates a new virtual environment named `venv` in the current directory, usually this will be your project's directory.

```
# Windows
python -m venv venv

# MacOS Terminal
python3 -m venv venv
```

### Activate Virtual Environment

The following commands activate an existing virtual environment on Windows and Unix systems. The command assume that the virtual environment is named `venv` and that its location is in the current directory.

```
# Windows
venv\Scripts\activate.bat

# MacOS Terminal
source venv/bin/activate
```

### Install Dependencies in Virtual Environment

To install dependencies in the current environment from a `requirements.txt` file the command below can be used.

```
# Windows
pip install -r requirements.txt

# MacOS Terminal
pip3 install -r requirements.txt
```

### Install Dependencies from npm

To install the required dependencies from npm, you will need to have `NodeJS` installed. Do run `npm install` to install the required dependencies for the project.

### Building the project using Docker

To build the project that is in docker currently, run `docker-compose build` and `docker-compose run --rm app django-admin startproject base .` to build the application.

### Running the Program

Once you have built finish the docker containers, you may run the docker containers by `docker-compose up` command in the terminal.

---

### Additional Dependencies

After installing additional dependencies from pip, you could view all dependencies using the `pip list` command, and also remember to `pip freeze > requirements.txt` to allow all team members to install all the additional dependencies that are needed for the project.
