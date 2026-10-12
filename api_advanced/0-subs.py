#!/usr/bin/python3
"""Returns the total number of subscribers for a subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return subscriber count, or 0 if the subreddit is invalid."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "alu-scripting-api-advanced/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json().get("data", {}).get("subscribers", 0)
