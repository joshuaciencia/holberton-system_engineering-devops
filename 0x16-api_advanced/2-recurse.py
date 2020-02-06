#!/usr/bin/python3
"""
queries the Reddit API and returns the titles
all hot articles for a given subreddit
"""
import requests as r


def recurse(subreddit, hot_list=[], after=''):
    """ all hot articles of a subreddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {
            'User-Agent': 'joshuaciencia'
            }
    if after is None:
        return hot_list
    req = r.get(url, headers=headers,
                allow_redirects=False,
                params={'after': after})
    if req.status_code != 200:
        return None
    data = req.json().get('data').get('children')
    hot_list += data
    after = req.json().get('data').get('after')
    return recurse(subreddit, hot_list, after)
