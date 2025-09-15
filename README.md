# Aurigae Moon Phases API

A simple Flask-based API that provides moon phase information for a given date.

## Features

- Returns moon illumination percentage and phase name/icon for a specified date
- Calculates upcoming main moon phases (new, first quarter, full, last quarter)
- Docker-ready for easy deployment

## Requirements

- Python 3.13+
- [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (optional)

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/aurigae_moonphases.git
cd aurigae_moonphases
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
export FLASK_APP=app/main.py
flask run --host=0.0.0.0 --port=5050
```

The API will be available at `http://localhost:5050`.

## Usage

Send a GET request to `/moonphase?date=YYYY-MM-DD`.

**Example:**

```bash
curl "http://localhost:5050/moonphase?date=2025-09-15"
```

**Response:**
```json
{
  "date": "2025-09-15",
  "illumination_percent": 73.2,
  "phase": "Waxing Gibbous",
  "icon": "🌔",
  "next_phases": {
    "new_moon": "2025-09-29",
    "first_quarter": "2025-09-07",
    "full_moon": "2025-09-15",
    "last_quarter": "2025-09-22"
  }
}
```

## Docker

Build and run the container:

```bash
docker build -t aurigae-moonphases .
docker run -p 5050:5050 aurigae-moonphases
```

## Project Structure

```
app/
  main.py
  ...
requirements.txt
Dockerfile
.gitignore
README.md
```

## License

MIT