#!/usr/bin/python3
"""Queries reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Query reddit API recursively"""
    if after == None:
        return hot_list
    base_url = 'https://www.reddit.com'
    try:
        resp = requests.get(
            url=f'{base_url}/r/{subreddit}/hot.json?limit=100',
            headers={"User-Agent": "myPyscript"},
            allow_redirects=False)
        data = resp.json()
        posts = data['data']['children']
        hot_list.append(posts['data']['title'])
    except Exception:
        return None