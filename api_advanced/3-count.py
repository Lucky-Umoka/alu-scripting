#!/usr/bin/python3
"""Recursively counts keyword occurrences in hot post titles."""
import requests


def count_words(subreddit, word_list, after=None, counts=None):
    """Print sorted keyword counts from hot post titles.

    Prints nothing if the subreddit is invalid or no keywords match.
    """
    if counts is None:
        counts = {}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting-api-advanced/1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return
    data = response.json()["data"]
    for post in data["children"]:
        for token in post["data"]["title"].lower().split():
            counts[token] = counts.get(token, 0) + 1
    if data["after"] is not None:
        return count_words(subreddit, word_list, data["after"], counts)
    totals = {}
    for word in word_list:
        key = word.lower()
        totals[key] = totals.get(key, 0) + counts.get(key, 0)
    for word, total in sorted(totals.items(), key=lambda x: (-x[1], x[0])):
        if total > 0:
            print("{}: {}".format(word, total))
