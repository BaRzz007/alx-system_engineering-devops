#!/usr/bin/python3
""" Queries reddit api and returns the number of subscribers """
import requests


def number_of_subscribers(subreddit):
    """ main function """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    resp = requests.get(
            url,
            allow_redirects=False,
            headers={"User-Agent": "Script by FizzBaRzz"})
    if resp.status_code >= 400 and resp.status_code <= 499:
        return 0
    resp = resp.json()
    return resp["data"]["subscribers"]
