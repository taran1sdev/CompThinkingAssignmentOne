from heapq import heapify, heappop, heappush

def dijkstra(graph, source):
        
    # We start by assuming the distance to every node is inf
    distances = {node: float("inf") for node in graph}
        
    # The distance from the source is 0
    distances[source] = 0
        
    pq = [(0, source)]
    heapify(pq)

    # We store visited nodes in a set
    visited = set()

    while pq:
        current_distance, current_node = heappop(pq)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbour, weight in graph[current_node].items():
            # Calculate distance to neighbours
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heappush(pq, (distance, neighbour))
    return distances
