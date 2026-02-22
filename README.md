# hand-made-by-django
An e-commerce website for selling handmade products using Django.

## Docker Setup

### 1) Files added for containerization
- `Dockerfile`
- `.dockerignore`
- `docker-entrypoint.sh`
- `docker-compose.yml`
- `.env.example`
- `requirements.txt`

### 2) Create your local environment file
```bash
cp .env.example .env
```

Update values in `.env`:
- `DJANGO_SECRET_KEY`: set a strong secret
- `DJANGO_DEBUG`: `False` for production-like runs
- `DJANGO_ALLOWED_HOSTS`: comma-separated hosts
- `SQLITE_NAME`: sqlite DB file path inside container (`/app/db.sqlite3`)

### 3) Build and run with Docker Compose
```bash
docker compose up --build
```

App URL: `http://localhost:8000`

### 4) What the container does on startup
`docker-entrypoint.sh` runs:
1. `python manage.py migrate --noinput`
2. `python manage.py collectstatic --noinput`
3. Starts Gunicorn server (`backend.wsgi:application`)

## GitHub Actions CI/CD Setup

### 1) Workflow file added
- `.github/workflows/ci-cd.yml`

### 2) What this pipeline does
On `pull_request` to `main/master`:
1. Install dependencies
2. Run migrations
3. Run Django tests
4. Build Docker image (without pushing)

On `push` to `main/master`:
1. Run tests
2. Build Docker image
3. Push image to Docker Hub

### 3) Required GitHub Secrets
In GitHub repo: `Settings -> Secrets and variables -> Actions`, add:
1. `DOCKERHUB_USERNAME`
2. `DOCKERHUB_TOKEN`

`DOCKERHUB_TOKEN` should be a Docker Hub access token (recommended), not your password.

### 4) Docker image naming
Image name is built as:
`<DOCKERHUB_USERNAME>/handmade-django`

Tags pushed:
- `latest` (default branch pushes)
- `sha-<commit>`

## Manual Docker Commands (without Compose)

Build:
```bash
docker build -t handmade-django:local .
```

Run:
```bash
docker run --rm -p 8000:8000 --env-file .env handmade-django:local
```
