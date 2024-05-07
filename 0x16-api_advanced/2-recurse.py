#!/usr/bin/python3
""" Contains recurse function """
import requests
import sys
after = None


def recurse(subreddit, hot_list=[]):
    """ Returns a list of titles of all hot posts on a given subreddit """
    global after
    headers = {'User-Agent': 'My-User-Agent'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)

    if response.status_code == 200:
        next_ = response.json().get('data').get('after')
        if next_ is not None:
            after = next_
            recurse(subreddit, hot_list)
        list_titles = response.json().get('data').get('children')
        for title_ in list_titles:
            hot_list.append(title_.get('data').get('title'))
        return hot_list
    else:
        return (None)
