# Django SMS Application

IT 120 – Integrative Programming and Technologies group assignment. The application will let a user compose an SMS, send it through an SMS provider, and see the result.

## Technologies

- Python 3.13 and Django 5.2 LTS
- SQLite for local development
- HTML/CSS and an SMS provider in later phases

## Local setup on Windows

### PowerShell

Open PowerShell in the project folder. For a fresh checkout, create the virtual environment and install the dependencies.

```powershell
py -3.13 -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

In each new PowerShell session, set a local Django secret key, check the project, and start Django. The key is generated for that session. The migration command creates the local SQLite database and applies any pending migrations.

```powershell
$env:DJANGO_SECRET_KEY = .\venv\Scripts\python.exe -c "import secrets; print(secrets.token_urlsafe(50))"
.\venv\Scripts\python.exe manage.py check
.\venv\Scripts\python.exe manage.py migrate
.\venv\Scripts\python.exe manage.py runserver
```

### Git Bash

Open Git Bash in the project folder. For a fresh checkout, create the virtual environment. If `venv/` already exists, skip the first command.

```bash
py -3.13 -m venv venv
source venv/Scripts/activate
python -m pip install -r requirements.txt
```

With the virtual environment active, run these commands in each new Git Bash session.

```bash
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')"
python manage.py check
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ to see the Django welcome page. Press Ctrl+C to stop the server.

## Development status

Phase 1 sets up the Django project, registers the `sms_app` app, and uses Django's default SQLite database. The SMS form and provider integration are planned for later phases.
