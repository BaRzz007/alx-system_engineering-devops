#!/usr/bin/python3
"""
Recurse module
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Queries the Reddit api recuresively and returns a list containing
    the titles of all hot articlesfor a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?"
    params = {
            "count": count,
            "limit": 100
            }

    if after is None and count > 0:
        return hot_list

    if after is not None:
        url = f"{url}after={after}"

    data = requests.get(
            url,
            allow_redirects=False,
            headers={"User-Agent": "FizzBaRzz's script"},
            params=params)
    if data.status_code >= 400 and data.status_code <= 499:
        return None

    data = data.json()
    post_data = data["data"]["children"]

    title_list = [post["data"]["title"] for post in post_data]
    return recurse(
            subreddit,
            hot_list + title_list,
            count + 100,
            data["data"]["after"])
