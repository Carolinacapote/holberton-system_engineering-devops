#!/usr/bin/python3
"""
Recursive function that queries the Reddit API and returns some information.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ Returns:
        - A list with the titles of all hot articles for a given subreddit.
        - None if no results are found.
    """

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    parameters = {'User-Agent': 'Mozilla', 'Content-Type': 'application/json'}

    request = requests.get(url, headers=parameters, params={'after': after},
                           allow_redirects=False)

    if request.status_code != 200:
        return None

    data = request.json().get('data')
    after = data.get('after')

    if after is None:
        return hot_list

    for item in data.get('children'):
        title = item.get('data').get('title')
        hot_list.append(title)

    return recurse(subreddit, hot_list, after)
