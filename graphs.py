# # BFS code for adjacency list
# from collections import deque

# def bfs(graph,start):
#     visited=set()
#     queue=deque([start])

#     while queue:
#         vertex = queue.popleft()
#         if vertex not in visited:
#             print(vertex,end=" ")
#             visited.add(vertex)
#             queue.extend(neighbor for neighbor in graph[vertex]if neighbor not in visited)

# graph={
#     'A':['B','C'],
#     'B':['D','E'],
#     'C':['F'],
#     'D':[],
#     'E':['F'],
#     'F':[]

# }
# print("BFS Traversal starting from vertex A:")
# bfs(graph,'A')


# DFS code for adjacency list
def dfs(graph, start):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(reversed([neighbor for neighbor in graph[vertex] if neighbor not in visited]))

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS Traversal starting from vertex A:")
dfs(graph, 'A')

