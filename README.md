# django-code-vault

## Refer this blog
```
https://medium.com/@meet_patel/pytest-a-comprehensive-guide-to-automated-testing-part-3-dd07869d3ef0
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
### Run all testcases:
``` 
pytest
```
