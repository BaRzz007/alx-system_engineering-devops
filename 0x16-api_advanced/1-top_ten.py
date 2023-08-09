#!/usr/bin/python3
""" Queries reddit api and prints the title of the first 10 hot posts
listed for a given subreddit """
import requests


def top_ten(subreddit):
    """ main function """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    data = requests.get(
            url,
            allow_redirects=False,
            headers={"User-Agent": "FizzBaRzz's script"})
    if data.status_code >= 400 and data.status_code <= 499:
        print(None)
    else:
        data = data.json()
        data = data["data"]["children"]
        for post in data:
            print(post["data"]["title"])
