# Web Exposure Scanner V2

A modular, high-performance reconnaissance framework for surface analysis and web exposure detection.

## Features

- **Async Subdomain Enumeration** — DNS brute-forcing with wildcard detection
- **Directory Brute-Forcing** — Async HTTP path scanning with status filtering
- **Port Scanning** — TCP SYN probes with service fingerprinting
- **Misconfiguration Detection** — Finds exposed configs, debug pages, sensitive files
- **Screenshot Capture** — Visual mapping of discovered endpoints
- **Structured Reports** — JSON, HTML, and PDF exports with severity scoring
- **Scan History** — Track exposure changes over time with trend analysis
- **Professional Dashboard** — Dark theme UI with real-time status updates

## Tech Stack

**Backend:** Python 3.11+, FastAPI, AsyncIO
**Database:** PostgreSQL with SQLAlchemy ORM
**Frontend:** React 18, TypeScript, Tailwind CSS
**Tools:** Chromium for screenshots, CVSS-like severity scoring

## Quick Start

```bash
cp .env.example .env
docker-compose up -d
```

Access the dashboard at `http://localhost:3000`
API available at `http://localhost:8000`
