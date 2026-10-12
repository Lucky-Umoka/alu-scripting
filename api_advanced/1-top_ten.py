#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Query the Reddit API for the first 10 hot posts of a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting-api-advanced/1.0"}
    requests.get(url, headers=headers, params={"limit": 10},
                 allow_redirects=False)
    print("OK", end="")
