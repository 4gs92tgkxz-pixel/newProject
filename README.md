# NHL Scores Fetcher

This small Python CLI fetches the latest NHL hockey scores using the public NHL Stats API (no API key required).

Usage

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run (default fetches today and 1 day back):

```bash
python3 app.py
```

Fetch last 3 days and print JSON:

```bash
python3 app.py --days 3 --json
```

Files

- `app.py`: main script
- `requirements.txt`: python deps

Next steps

- Add a web UI or simple dashboard
- Add scheduling (cron) or a background worker to poll frequently
- Add caching or a database if you need historical queries
 
Web UI

Run the Flask web UI (after installing dependencies):

```bash
python3 web.py
```

Open http://localhost:5000 in your browser. Use the Days input and Refresh button to fetch recent scores.
# newProject
new project
