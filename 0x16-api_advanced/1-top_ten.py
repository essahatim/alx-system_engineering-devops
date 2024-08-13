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
        Prints the titles of the first 10 hot posts
        None if the subreddit is invalid.
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "OkSatisfaction9309"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        titles = response.json().get("data").get("children")
        for post in titles:
            print(post.get("data").get("post"))
    else:
        return (None)
