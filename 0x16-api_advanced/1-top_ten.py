#!/usr/bin/python3
""" this module contains the function top_ten """
import requests
import sys


def top_ten(subreddit):
    """ returns the top ten posts for a given subreddit """
    headers = {'User-Agent': 'My-User-Agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        titles_ = response.json().get('data').get('children')
        for title_ in titles_:
            print(title_.get('data').get('title'))
    else:
        print(None)
