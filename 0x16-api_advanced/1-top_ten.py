#!/usr/bin/python3
"""
This module queries the Reddit API and prints some information.
"""
import requests


def top_ten(subreddit):
    """ It prints:
        - the titles of the first 10 hot posts listed for a given subreddit.
        - 0 if not a valid subreddit.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    parameters = {'User-Agent': 'Mozilla', 'Content-Type': 'application/json'}

    request = requests.get(url, headers=parameters, allow_redirects=False)

    if request.status_code != 200:
        print('None')
        return

    data = request.json().get('data')

    for item in data.get('children'):
        title = item.get('data').get('title')
        print(title)
