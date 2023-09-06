# API

## About

API - Python Backend Challenge

Tech Stack:

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [SQLite](https://www.sqlite.org/index.html)
- [SQLAlchemy](https://www.sqlalchemy.org)
- [Pydantic](https://docs.pydantic.dev/latest/)
- [Docker](https://www.docker.com/)

## Hosting

This app is hosted via FL0.
[This is the link](https://technical-evaluation-rd-jwc2-dev.fl0.io/)

## Note for Credentials

The credentials can be change in src/auth/auth.py line 10 and 11.
The default credentials are:

- `user`: admin
- `password`: password

## Installation

```bash
git clone https://github.com/NoSquazer/Technical-Evaluation-RD.git
```

## Note for Windows users

If you are using Windows, maybe the **entrypoint.sh** use a different end of line character.

- Check the end of line character of the **entrypoint.sh** file, it should be **LF**.
- If it is not LF, change it to LF.
- In VSCode you can change it in the bottom right corner. It should say **CRLF**, click on it and change it to **LF**.

### Setup for local development

```bash
docker compose -f docker-compose-dev.yml up --build
```

## API Routes

### Route 1: /api/db/input/{my_target_field}

- Method: POST
- Parameters:
- `field_1`: Some data.
- `author`: Some author data.
- `description`: Even more data.
- `my_numeric_field`: A number.

- Example Request:

```bash
  POST /api/db/input/description
```

- Body:

```bash
  {
  "field_1": "Argentino",
  "author": "Roberto",
  "description": "Nació en Córdoba, Argentina y le gusta el mate.",
  "my_numeric_field": 42
  }
```

- Example Response:

```bash
  {
  "id": 1
  }
```

### Route 2: /api/db/get_data/{id}

- Method: GET
- Parameters:
- `id`: Id of the data to get.

- Example Request:

```bash
  GET /api/db/get_data/1
```

- Example Response:

```bash
  {
  "id": 1,
  "field_1": "Argentino",
  "author": "Roberto",
  "description": "NACIÓ EN CÓRDOBA, ARGENTINA Y LE GUSTA EL MATE.",
  "my_numeric_field": 42
  }
```
