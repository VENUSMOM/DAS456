Here's the completed implementation of the Dijkstra algorithm in Python:

```python
import heapq

def dijkstra(graph, start, target):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    unvisited = [(0, start)]
    previous = {node: None for node in graph}

    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)
        
        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            return path[::-1], distances[target]
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(unvisited, (distance, neighbor))
    
    return None

# Test the implementation
graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}

path_A_to_F, distance_A_to_F = dijkstra(graph, 'A', 'F')
path_B_to_G, distance_B_to_G = dijkstra(graph, 'B', 'G')

print("Shortest path from A to F:", path_A_to_F)
print("Shortest distance from A to F:", distance_A_to_F)

print("Shortest path from B to G:", path_B_to_G)
print("Shortest distance from B to G:", distance_B_to_G)
```

This code will output the shortest paths and distances between nodes A-F and B-G according to the provided graph.