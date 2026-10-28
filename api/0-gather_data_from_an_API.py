#!/usr/bin/python3
"""Returns information about an employee's TODO list progress."""
import json
import sys
import urllib.request


def fetch(url):
    """Fetch and decode JSON from a URL."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = fetch("{}/users/{}".format(base_url, employee_id))
    todos = fetch("{}/todos?userId={}".format(base_url, employee_id))

    done = [t["title"] for t in todos if t["completed"]]

    print("Employee {} is done with tasks({}/{}):".format(
        user["name"], len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
