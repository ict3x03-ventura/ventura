# Ventura

## Requirements

- `python` ^3.6
- `pip`
- `virtualenv` (_just `pip install virtualenv` if don't have_)
- PostgreSQL 
- pgAdmin (_optional_)

## Installation

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

### Initialising the Database
To initialise the database, run the following command:
```
python manage.py migrate
```

### Running the Program

Once you activated your virtual environment, you can run the program. To run the program, run `python manage.py runserver` in the terminal and navigate to the localhost stated in the terminal

---

### Additional Dependencies

After installing additional dependencies from pip, you could view all dependencies using the `pip list` command, and also remember to `pip freeze > requirements.txt` to allow all team members to install all the additional dependencies that are needed for the project.