# django-code-vault

## Refer this blog
```
https://medium.com/@meet_patel/6285888c31d7
```
## Getting started:
### Clone this repository:
```
git clone https://github.com/scalereal/django-code-vault.git
```
### Install pipenv
```
pip install pipenv
```
### Activate environment:
```
pipenv shell
```
### Install dependencies:
```
pipenv install
```
### create database in postgres:
```
CREATE DATABASE django_code_vault;
```
### create environment variables
```
Create a .env file by copying the .env.example file.
After copying the contents, edit the SECRET_KEY with your respective secret key.
In DATABASE_URL, replace your_database_user and your_database_password with your respective Database User and Password.
```
### Start the server:
``` 
python manage.py runserver
```

### Run testcase using coverage command:
``` 
coverage run -m pytest
```

### Get coverage report:
``` 
coverage html
```
