#!/usr/bin/python3
"""
queries the Reddit API and returns the titles
all hot articles for a given subreddit
"""
import requests as r


def recurse(subreddit, hot_list=[], idx=0, after=None):
    """ all hot articles of a subreddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {
            'User-Agent': 'joshuaciencia'
            }
    req = r.get(url, headers=headers,
                allow_redirects=False,
                params={'after': after})
    if req.status_code != 200:
        return hot_list
    data = req.json().get('data').get('children')
    after = req.json().get('data').get('after')
    try:
        title = data[idx].get('data').get('title')
        hot_list.append(title)
        return recurse(subreddit, hot_list, idx + 1, after)
    except IndexError:
        return recurse(subreddit, hot_list, 0, after)
