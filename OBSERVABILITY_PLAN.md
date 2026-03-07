# Observability Implementation Plan: Phase 1 (Django Metrics)

This document outlines the steps to instrument the `articraft-django` application for Prometheus monitoring.

## 1. Dependencies
Add the following to `requirements.txt`:
```text
django-prometheus==2.3.1
```

## 2. Django Settings (`backend/settings.py`)

### Apps
Add `django_prometheus` to `INSTALLED_APPS`.

### Middleware
Prometheus needs to "wrap" the entire request/response cycle.
- **Top:** `django_prometheus.middleware.PrometheusBeforeMiddleware`
- **Bottom:** `django_prometheus.middleware.PrometheusAfterMiddleware`

### Database
To track DB query latencies, we change the engine in `DATABASES`. Since we use `dj-database-url`, we will wrap the result:
```python
# In settings.py
DATABASES = {
    'default': dj_database_url.config(...)
}
# Wrap the engine for Prometheus
DATABASES['default']['ENGINE'] = 'django_prometheus.db.backends.postgresql'
```

## 3. URLs (`backend/urls.py`)
Add the endpoint that Prometheus will scrape:
```python
path('', include('django_prometheus.urls')),
```

## 4. System Design: Why this order?
- **BeforeMiddleware:** Starts the clock as soon as a request hits Django.
- **AfterMiddleware:** Stops the clock after all processing (including templates and DB) is done.
- **DB Wrapper:** Intercepts every SQL call to measure how long the RDS instance takes to respond.

## 5. Verification
After applying these changes:
1. Run `docker compose up --build`.
2. Visit `http://localhost:8000/prometheus/metrics`.
3. You should see a list of metrics starting with `django_http_requests_total_by_method_total`.
