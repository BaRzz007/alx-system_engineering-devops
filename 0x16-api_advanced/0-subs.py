#!/usr/bin/python3
"""Queries reddit api"""
import requests


def number_of_subscribers(subreddit):
    """Queries reddit api and returns number of subscribers
    for a given subreddit"""
    try:
        resp = requests.get(
            url=f'https://www.reddit.com/r/{subreddit}/about.json',
            headers={"User-Agent": "myPyscript"},
            allow_redirects=False)

        data = resp.json()
        return data['data']['subscribers']
    except Exception:
        return 0
