#!/usr/bin/python3
"""
Returning the number of subscribers of Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns:
        - NUmber of subscribers.
        - 0 if an invalid subreddit is given.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    parameters = {'User-Agent': 'Mozilla', 'Content-Type': 'application/json'}

    request = requests.get(url, headers=parameters, allow_redirects=False)

    if request.status_code != 200:
        return 0

    data = request.json().get('data')
    subscribers = data.get('subscribers')

    return subscribers
