graph = [[1, 3],
         [0],
         [3],
         [2, 0],
         []]
passed = [False for i in range(len(graph))]


def dfs(i):
    if passed[i]:
        return
    passed[i] = True
    print(i + 1, end=" ")
    for i2 in graph[i]:
        dfs(i2)


for i in range(len(graph)):
    dfs(i)
