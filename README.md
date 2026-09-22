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
- `Nilesh_cycleGAN_dehaze_saved_model/`: default TensorFlow SavedModel
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