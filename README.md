# API

## About

API - Python Backend Challenge

Technologies used:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [MongdoDB](https://www.mongodb.com/)

## Installation

```bash
git clone git@github.com:huntekapp/api.git
```

### Create .env file

```bash
cp .env.example .env
```

### Instrall requirements

```bash
pip install -r requirements/requirements.txt
```

### Setup for local development

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

## API Routes

### Route 1: /api/month/resume

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:

```bash
  GET /api/month/resume?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  {
  "id": 0
  }
```

### Route 2: /api/month/billing

- Method: GET
- Parameters:
- `month`: Month in MM-YYYY format.
- `company`: Business name or identifier.

- Example Request:

```bash
  GET /api/month/billing?month=05-2023&company=623a020283ecc98fe0bf34e2
```

- Example Response:

```bash
  {
  "id": 0,
  "field_1": "string",
  "author": "string",
  "description": "string",
  "my_numeric_field": 0
  }
```
