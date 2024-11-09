from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    dfs_result.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    bfs_result.append(start)

    while queue:
        v = queue.popleft()
        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                bfs_result.append(neighbor)


n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for edges in graph:
    edges.sort()

dfs_result = []
bfs_result = []

visited_dfs = [False] * (n + 1)
dfs(graph, visited_dfs, v)

visited_bfs = [False] * (n + 1)
bfs(graph, visited_bfs, v)

print(" ".join(map(str, dfs_result)))
print(" ".join(map(str, bfs_result)))