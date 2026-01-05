#!/usr/bin/env python3
"""Fetch latest NHL hockey scores using the public NHL Stats API.

Usage:
  python3 app.py [--days N] [--json]

By default fetches games from today and N days back (default N=1).
"""
import argparse
import datetime
import json
import sys
from typing import List, Dict

import requests


def fetch_scores(days: int = 1) -> List[Dict]:
    today = datetime.date.today()
    start = today - datetime.timedelta(days=days)
    start_str = start.isoformat()
    end_str = today.isoformat()

    url = (
        f"https://statsapi.web.nhl.com/api/v1/schedule?startDate={start_str}&endDate={end_str}"
    )
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    games = []
    for date_obj in data.get("dates", []):
        date_str = date_obj.get("date")
        for game in date_obj.get("games", []):
            game_pk = game.get("gamePk")
            status = game.get("status", {}).get("detailedState")

            home = game.get("teams", {}).get("home", {})
            away = game.get("teams", {}).get("away", {})

            item = {
                "gamePk": game_pk,
                "date": date_str,
                "status": status,
                "home": {
                    "name": home.get("team", {}).get("name"),
                    "score": home.get("score"),
                },
                "away": {
                    "name": away.get("team", {}).get("name"),
                    "score": away.get("score"),
                },
            }
            games.append(item)

    return games


def pretty_print(games: List[Dict]):
    if not games:
        print("No games found for the requested range.")
        return

    for g in games:
        home = g["home"]
        away = g["away"]
        status = g.get("status")
        date = g.get("date")
        print(f"{date} | {away['name']} {away['score']} - {home['score']} {home['name']} | {status} | id={g['gamePk']}")


def main(argv=None):
    parser = argparse.ArgumentParser(description="Fetch latest NHL hockey scores.")
    parser.add_argument("--days", type=int, default=1, help="How many days back (inclusive) to fetch (default 1)")
    parser.add_argument("--json", action="store_true", help="Print raw JSON output")
    args = parser.parse_args(argv)

    try:
        games = fetch_scores(days=args.days)
    except requests.RequestException as e:
        print(f"Error fetching scores: {e}", file=sys.stderr)
        sys.exit(2)

    if args.json:
        print(json.dumps(games, indent=2))
    else:
        pretty_print(games)


if __name__ == "__main__":
    main()
