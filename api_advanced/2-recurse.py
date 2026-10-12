#!/usr/bin/python3
"""Recursively collects titles of all hot posts for a subreddit."""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """Return a list of all hot post titles, or None if none are found."""
    if hot_list is None:
        hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting-api-advanced/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    data = response.json()["data"]
    for post in data["children"]:
        hot_list.append(post["data"]["title"])
    if data["after"] is None:
        return hot_list if hot_list else None
    return recurse(subreddit, hot_list, data["after"])
