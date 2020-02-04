#!/usr/bin/python3
""" Dictionary of list of dictionaries """
from json import dumps
from requests import get

if __name__ == "__main__":
    todo_list = get("https://jsonplaceholder.typicode.com/todos").json()
    users = get("https://jsonplaceholder.typicode.com/users/").json()
    output = {}
    for user in users:
        id = user.get("id")
        name = user.get("username")
        todo = []
        for d in todo_list:
            if d.get("userId") == id:
                tit = d.get("title")
                status = d.get("completed")
                todo.append({
                    "task": tit,
                    "completed": status,
                    "username": name})
        output[str(id)] = todo
    f_name = "todo_all_employees.json"
    with open(f_name, "w") as f:
        f.write(dumps(output)+"\n")
