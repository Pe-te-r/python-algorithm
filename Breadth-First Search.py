from collections import deque

def search(tree,start):
    frontier=deque[start]
    visited=set()

    while frontier:
        node=deque.popleft(frontier)

        if node not in visited:
            frontier.extend(tree.get(node,[]))

    print(visited)


simple_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G','Z'],
    'Z':['X','Y'],
    'X':[],
    'Y':[],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}

search(simple_tree,'A')

