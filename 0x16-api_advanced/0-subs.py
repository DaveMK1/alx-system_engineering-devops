#!/usr/bin/python3.4
"""
Function that queries the Reddit API
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.

    Arguments:
        subreddit: A string representing the subreddit name.

    Returns:
        The number of subscribers for the subreddit. If the subreddit
        is invalid or if there's any error, returns 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "MyUniqueAPI/1.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
