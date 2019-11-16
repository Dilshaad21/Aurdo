# Aurdo

## Theme
This is an order accepting app which doesn’t require any operator or receptionist. The basic idea is to get users’ orders in the form of an audio file and then process it accordingly. It is actually a seller oriented app.

## Technology Stack
### Components
- HTML, CSS: making views and styling wepages
- Bootstrap: for styling webpages
- Javascript: for making dynamic frontend
- Python: language used as a major part in the framework
- sqlite3: for database management

## Requirements
- Django --version >=2
- Python --version >=3.5

## How to delpoy ?

- Create a virtual env using `conda`,`pip` or `virtualenv`.
- Install `django` after activating virtual environment.
- Install libraries `pandas`,`numpy`,`matplotlib` using `pip install`<library_name> in virtual env.
- Run migrations using `python manage.py makemigrations`.
- After running migrations run `python manage.py migrate`.
- Now, run `python manage.py runserver` to run it in `localhost:8000`.
