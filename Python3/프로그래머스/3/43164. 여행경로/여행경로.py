from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for a, b in sorted(tickets, reverse=True):
        graph[a].append(b)

    stack = ['ICN']
    path = []

    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        path.append(stack.pop())

    return path[::-1]