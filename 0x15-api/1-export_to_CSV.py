#!/usr/bin/python3
""" Export to CSV """
import requests as r
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    todo = r.get("https://jsonplaceholder.typicode.com/todos")
    name = r.get("https://jsonplaceholder.typicode.com/users/" + id)
    data = todo.json()
    tasks = []
    for d in data:
        if d.get("userId") == int(id):
            tasks.append((d.get("title"), d.get("completed")))
    f_name = id + ".csv"
    name = name.json().get("username")
    with open(f_name, "w") as f:
        for t in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(id, name, t[1], t[0]))
