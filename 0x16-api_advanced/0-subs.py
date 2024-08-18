#!/usr/bin/python3
"""Function that queries the reddit API"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit: The name of the subreddit to query
    Returns:
        The number of subscribers to the subreddit
        0 in error
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'user-agent': 'OkSatisfaction9309'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return (0)
    return ((response.json().get("data").get("subscribers"))
