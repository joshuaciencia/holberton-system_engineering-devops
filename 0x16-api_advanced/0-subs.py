#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
"""
import requests as r


def number_of_subscribers(subreddit):
    """ subscribers of a subreddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    headers = {
            'User-Agent': 'joshuaciencia'
            }
    req = r.get(url, headers=headers, allow_redirects=False)
    if req.status_code != 200:
        return 0
    return req.json().get('data').get('subscribers')
