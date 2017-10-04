import queue

graph = [  # список смежности
    [1, 3],
    [0, 3, 4, 5],
    [4, 5],
    [0, 1, 5],
    [1, 2],
    [1, 2, 3]
]
passed = [False for i in range(len(graph))]
q = queue.Queue()


def bfs(i):
    if passed[i]:
        return
    q.put(i)
    passed[i] = True
    while not q.empty():
        j = q.get()
        print(j + 1, end=' ')
        for i2 in graph[j]:
            if passed[i2]:
                continue
            q.put(i2)
            passed[i2] = True


for i in range(len(graph)):
    bfs(i)
