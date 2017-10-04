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


if __name__ == "__main__":
    print("Алгоритма поиска в глубину в графе\n","Для графа в виде списка смежности",graph)
    for i in range(len(graph)):
        dfs(i)
