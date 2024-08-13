#!/usr/bin/python3
"""Function that queries the reddit API"""
import json
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit: The name of the subreddit to query
    Returns:
        The number of subscribers to the subreddit
        0 in error
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "OkSatisfaction9309"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    else:
        return (0)
