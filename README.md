# Appointment
A website for appointment

## Setup Environment
It's highly recomended to setup django in a virtual environment

### Setup virtual environment
Create a python virtual environment with `venv` package

```
$ python -m venv <environment name>
```

### Activate the virtual environment
Source the appropriate environment activation script depending on your shell.

```
$ source /path/to/environment/bin/activate
```

Note: `activate` without any suffix is for `Bash` shell.

### Installing Django
Install django in the virtual environment with the following command:

```
$ pip install -r requirements.txt
```
## Migrate
Do migration only once before starting the server, or after any change to the database model with

```
python hospitalmgmt/manage.py migrate [port]
```


## Running the server
Run the server with the following code inside the virtual environment:

```
python hospitalmgmt/manage.py runserver [port]
```
