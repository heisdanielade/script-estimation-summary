# SCRUM Cycle Estimation Summary

![Python](https://img.shields.io/badge/python-3.10+-blue)

A Python script that connects to the Plane.so API and calculates the total estimation points for a given SCRUM cycle. Designed with clean OOP structure, error handling, and basic test coverage.

## Core Functionality:

- Connect to the Plane.so API
- Fetch tasks/issues in a specific SCRUM cycle
- List issues with their `priority`, `estimate point` & `timelines`
- Extract and sum estimation points

## Setup

1. Clone the repo

```bash
    git clone https://github.com/heisdanielade/script-estimation-summary
    cd script-estimation-summary
```

2. Create .env file

```env
    PLANE_BASE_URL=https://api.plane.so/api/v1
    PLANE_API_KEY=<your-plane.so-api-key>
    WORKSPACE_SLUG=<workspace-name>
    PROJECT_ID=<project-uuid>
    CYCLE_ID=<cycle-uuid>
```

3. Install dependencies

```bash
    pip install -r requirements.txt
```

## Usage

Run:

```bash
    python main.py
```

## Tests

```bash
    pytest -v
```

---
