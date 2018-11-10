from collections import deque

# init test data
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["alice"] = ["peggy"]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["jony", "thom"]
graph["peggy"] = []
graph["jony"] = []
graph["anuj"] = []
graph["thom"] = []


# end init test data


def check(name):
    return name[-1] == "m"


def breath_search(name):
    search_que = deque()
    search_que += graph[name]
    while search_que:
        tem_people = search_que.popleft()
        if check(tem_people):
            return tem_people
        search_que += graph[tem_people]
    return None


print(breath_search("you"))

