#!/usr/bin/python3
"""Queries reddit api"""
import requests


def top_ten(subreddit):
    """Gets and prints top ten hot posts for a given subreddit"""
    base_url = 'https://www.reddit.com'
    try:
        resp = requests.get(
            url=f'{base_url}/r/{subreddit}/hot.json?limit=10',
            headers={"User-Agent": "FizzBarzzPyscript"},
            allow_redirects=False)

        data = resp.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    except Exception:
        return None
