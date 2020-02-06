#!/usr/bin/python3
"""
ueries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""
import requests as r


def top_ten(subreddit):
    """ top ten hot posts of a subreddit """
    url = 'https://www.reddit.com/r/' + subreddit + '/hot.json'
    headers = {
            'User-Agent': 'joshuaciencia'
            }
    req = r.get(url, headers=headers, allow_redirects=False)
    if req.status_code != 200:
        print(None)
        return
    data = req.json().get('data').get('children')
    for d in data[:10]:
        print(d.get('data').get('title'))
