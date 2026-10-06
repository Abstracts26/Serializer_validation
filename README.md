# E-commerce

## Local configuration

Copy `.env.example` to `.env` and set `DJANGO_SECRET_KEY` to a private random
value. Set the database variables to match your local PostgreSQL instance.
The `.env` file is ignored by Git.

Load the variables in your shell before running Django commands:

```sh
set -a
. ./.env
set +a
python manage.py migrate
python manage.py runserver
```

Do not commit `.env`, database files, virtual environments, or Python cache
files.
