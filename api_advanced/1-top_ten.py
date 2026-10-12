#!/usr/bin/python3
"""Prints the titles of the first 10 hot posts of a subreddit."""
import requests


def top_ten(subreddit):
    """Print the first 10 hot post titles, or None if invalid."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "linux:alu_api_advanced:v1.0"}
    response = requests.get(url, headers=headers, params={"limit": 10},
                            allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    for post in response.json()["data"]["children"]:
        print(post["data"]["title"])
