# Multispectral Image Dehazing

A Django application for applying a trained CycleGAN dehazing model to uploaded images.

## Requirements

- Windows, macOS, or Linux
- Python 3.12 recommended
- 4 GB or more of available memory for TensorFlow and the model

## Quick start

From the repository root in PowerShell:

```powershell
cd dehazing_project
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py check
python manage.py runserver
```

Open http://127.0.0.1:8000/ in a browser.

The default database is the repository's SQLite file at `dehazing_project/db.sqlite3`. TensorFlow is loaded only when an image is processed.

## Send as a ZIP file

Before creating the ZIP, do not include `dehazing_project/.env`, `.git`, generated media, Python cache folders, or `.venv` unless there is a specific reason. The `.env` file may contain passwords, and a Windows virtual environment is machine-specific. This project's `.venv` is also approximately 1.6 GB.

### Recommended setup on the recipient's computer

1. Install Python 3.12 and make sure `py --version` works in PowerShell.
2. Extract the ZIP, then open PowerShell in the extracted repository folder.
3. Create a fresh environment and install the dependencies:

```powershell
cd .\dehazing_project
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

4. Keep the default `USE_POSTGRES=0` in `.env` to use SQLite. Do not copy the original `.env` from the development computer.
5. Initialize the database and verify the application:

```powershell
python manage.py migrate
python manage.py check
python manage.py runserver
```

6. Open `http://127.0.0.1:8000/`.

### If the ZIP includes `.venv`

The recipient should still preferably delete the included `.venv` and follow the fresh setup above. If both computers use Windows, the same Python 3.12 layout, and the extracted folder works with the environment's recorded paths, they can try:

```powershell
cd .\dehazing_project
.venv\Scripts\Activate.ps1
python --version
python manage.py migrate
python manage.py check
python manage.py runserver
```

If activation or imports fail, recreate `.venv`; the application files and `requirements.txt` are the portable parts. A copied environment is not portable across operating systems, Python versions, or different extraction paths.

### Share with another device

On the computer running Django, add its IPv4 address to `.env`, for example:

```dotenv
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.25
```

Then run:

```powershell
python manage.py runserver 0.0.0.0:8000
```

The other device opens `http://192.168.1.25:8000/`. Windows Firewall may need to allow Python on private networks.

## Share on a local network

To let another device on the same Wi-Fi or LAN open the application, find the host computer's IPv4 address with `ipconfig`, then run:

```powershell
python manage.py runserver 0.0.0.0:8000
```

Add the host computer's address to `DJANGO_ALLOWED_HOSTS` in `.env`:

```dotenv
DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,192.168.1.25
```

The other device can then open `http://192.168.1.25:8000/`. Allow Python or TCP port 8000 through Windows Firewall when Windows asks. This is suitable for a trusted local demonstration only; do not expose Django's development server directly to the public internet.

## Run as a local application server

For a more stable Windows demonstration server, use Waitress:

```powershell
waitress-serve --listen=0.0.0.0:8000 dehazing_project.wsgi:application
```

Use a real reverse proxy, HTTPS, secret management, and a production database before public deployment.

## Configuration

Copy `dehazing_project/.env.example` to `dehazing_project/.env`. The `.env` file is intentionally ignored by Git.

| Variable | Default | Purpose |
| --- | --- | --- |
| `DJANGO_SECRET_KEY` | development placeholder | Secret used by Django; replace it outside local development |
| `DJANGO_DEBUG` | `1` | Set to `0` for deployment |
| `DJANGO_SECURE_SSL` | `0` | Set to `1` only when HTTPS is configured; enables secure cookies, redirects, and HSTS |
| `DJANGO_ALLOWED_HOSTS` | `127.0.0.1,localhost` | Comma-separated hostnames or IP addresses |
| `DJANGO_CSRF_TRUSTED_ORIGINS` | empty | Comma-separated full origins such as `https://example.com` |
| `DEHAZING_MODEL_PATH` | repository model directory | Optional absolute path to another SavedModel |
| `USE_POSTGRES` | `0` | Set to `1` to use `DATABASE_URL` instead of SQLite |
| `DATABASE_URL` | empty | PostgreSQL connection URL when PostgreSQL is enabled |
| `POSTGRES_SSLMODE` | `prefer` | PostgreSQL SSL mode; use `require` when the server supports SSL |

## Project layout

- `dehazing_project/`: Django project and application
- `dehazing_project/dehazing_app/`: views, forms, model loader, and migrations
- `dehazing_project/templates/`: HTML templates
- `dehazing_project/static/`: CSS, JavaScript, and images
- `cycleGAN_dehaze_saved_model/`: default TensorFlow SavedModel
- `*.ipynb`: training and architecture notebooks

## Git workflow

Do not commit `.env`, passwords, API keys, generated media, `.venv`, Python caches, or local database files. Before pushing:

```powershell
git status
git add README.md LICENSE .gitignore dehazing_project
git commit -m "Prepare project for local deployment"
git push origin main
```

If your default branch is not `main`, replace it with the branch shown by `git branch --show-current`.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE). The trained model and research materials may have separate terms; verify those terms before redistributing them.