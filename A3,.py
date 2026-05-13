def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


# Input
arr = [64, 25, 12, 22, 11]

print("Original:", arr)
print("Sorted:", selection_sort(arr))

#Job scheduling

def job_scheduling(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * max_deadline
    profit = 0

    for job in jobs:
        for j in range(job[1] - 1, -1, -1):
            if slots[j] == -1:
                slots[j] = job[0]
                profit += job[2]
                break

    return slots, profit


# Input
jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

schedule, profit = job_scheduling(jobs)
print("Schedule:", schedule)
print("Total Profit:", profit)

#Dijkstra (Shortest Path)
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    pq = [(0, start)]

    while pq:
        current_dist, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            distance = current_dist + weight

            if distance < dist[neighbor]:
                dist[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return dist


# Input
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("Shortest distances from A:", dijkstra(graph, 'A'))

#4. Prim’s Algorithm (MST)
import heapq

def prim(graph, start):
    visited = set()
    pq = [(0, start)]
    total_cost = 0

    while pq:
        cost, node = heapq.heappop(pq)

        if node in visited:
            continue

        visited.add(node)
        total_cost += cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (weight, neighbor))

    return total_cost


# Input (same graph)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print("MST Cost (Prim):", prim(graph, 'A'))


#5. Kruskal’s Algorithm (MST

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  # path compression
    return parent[x]


def union(parent, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    parent[root_x] = root_y


def kruskal(edges, nodes):
    edges.sort(key=lambda x: x[2])

    parent = {node: node for node in nodes}
    total_cost = 0

    for u, v, w in edges:
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            total_cost += w

    return total_cost


# Input
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 1)
]

nodes = ['A', 'B', 'C', 'D']

print("MST Cost (Kruskal):", kruskal(edges, nodes))