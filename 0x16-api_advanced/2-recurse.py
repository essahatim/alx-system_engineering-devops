#!/usr/bin/python3
"""Function that queries the reddit API"""
import json
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """
    Args:
        subreddit: The name of the subreddit to query
        hot_list: A list to store the titles of hot articles
        after: The params for pagination
    Return:
        A list containing the titles of all hot posts
        None if the subreddit is invalid or not found
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'xica369'}
    params = {"after": after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get("data").get("after")
        children = data.get("children")
        if not children and not hot_list:
            return (None)
        if posts is not None:
            after = posts
            recurse(subreddit, hot_list)
        list_posts = response.json().get("data").get("children")
        for post in list_posts:
            hot_list.append(post.get("data").get("title"))
        return (hot_list)
    else:
        return (None)


