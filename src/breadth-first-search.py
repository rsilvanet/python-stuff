def isSalesman(name):
    if name == "claire" or name == "jonny":
        return True
    return False

def search(relations, start):
    from collections import deque
    queue = deque()
    queue += relations[start]
    verified = []

    while queue:
        person = queue.popleft()
        if not person in verified:
            verified.append(person)
            queue += relations[person]
            if isSalesman(person):
                print(person + " is a salesman")

relations = {}
relations["me"] = ["alice", "bob", "claire"]
relations["bob"] = [ "anuj", "peggy"]
relations["alice"] = ["peggy"]
relations["claire"] = ["thom", "jonny"]
relations["anuj"] = []
relations["peggy"] = []
relations["thom"] = []
relations["jonny"] = []

search(relations, "me")