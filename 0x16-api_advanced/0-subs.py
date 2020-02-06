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
    req = r.get(url, headers=headers)
    data = req.json().get('data').get('subscribers')
    return data if data is not None else 0