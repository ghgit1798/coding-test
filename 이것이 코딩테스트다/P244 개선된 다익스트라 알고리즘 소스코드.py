################################################################

## version 2
import heapq

def dijkstra(graph, start):
    # 그래프의 정점 수
    num_vertices = len(graph)

    # 시작 정점으로부터의 최단 거리를 저장하는 리스트
    distance = [float('inf')] * num_vertices
    distance[start] = 0

    # 방문한 정점을 저장하는 집합
    visited = set()

    # 시작 정점을 우선순위 큐에 삽입
    queue = [(0, start)]

    while queue:
        # 우선순위 큐에서 최단 거리가 가장 짧은 정점을 선택
        dist, current = heapq.heappop(queue)

        # 이미 방문한 정점이라면 건너뜀
        if current in visited:
            continue

        # 현재 정점을 방문한 것으로 표시
        visited.add(current)

        # 현재 정점과 인접한 정점들을 탐색
        for neighbor, weight in graph[current]:
            # 시작 정점에서 인접 정점까지의 거리
            new_distance = distance[current] + weight

            # 현재까지의 최단 거리보다 더 짧은 거리를 발견한 경우, 업데이트
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                # 우선순위 큐에 새로운 거리와 정점을 삽입
                heapq.heappush(queue, (new_distance, neighbor))

    return distance

#############################################################

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])
