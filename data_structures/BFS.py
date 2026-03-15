
from collections import deque

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}


def bfs(graph,start):

    queue = deque()

    queue.append(start)

    visited = set()
    visited.add(start)
    neightbors=list()
    neightbors.append(start)

    while len(queue)>0:
        current_high = queue.popleft()

        for neigbor in graph[current_high]:
            if neigbor not in visited:
                visited.add(neigbor)
                queue.append(neigbor)
                neightbors.append(neigbor)

    print(neightbors)
            
start = input ("Set start vertex:").upper()
try:
    if len(start)==1:
        bfs(graph,start)
except:
    print("Start vertex must be a letter:")
    start = input ("Set start vertex:")


    