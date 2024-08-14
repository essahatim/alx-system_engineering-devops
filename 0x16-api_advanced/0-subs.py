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
    headers = {'User-Agent': 'ResortDowntown2584'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json().get("data").get("subscribers")
        return (response.json().get("data").get("subscribers"))
    return (0)
