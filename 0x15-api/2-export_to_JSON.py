#!/usr/bin/python3
""" Export to JSON """
from json import dumps
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    todo = get("https://jsonplaceholder.typicode.com/todos")
    name = get("https://jsonplaceholder.typicode.com/users/" + id)
    data = todo.json()
    tasks = []
    name = name.json().get("username")
    for d in data:
        if d.get("userId") == int(id):
            tit = d.get("title")
            status = d.get("completed")
            tasks.append({"task": tit, "completed": status, "username": name})
    f_name = id + ".json"
    with open(f_name, "w") as f:
        f.write(dumps({id: tasks}))
