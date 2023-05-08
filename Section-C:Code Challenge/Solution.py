import sys
from heapq import heappush, heappop

def navigate(roads, start, end):
    graph = roads["graph"]
    nodes = graph["nodes"]
    edges = graph["edges"]

    adjacency_list = {node["id"]: [] for node in nodes}

    for edge in edges:
        source = edge["source"]
        target = edge["target"]
        distance = edge["metadata"]["distance"]
        adjacency_list[source].append((target, distance))
        adjacency_list[target].append((source, distance))

    heap = [(0, start)]
    visited = set()
    distances = {node["id"]: sys.maxsize for node in nodes}
    distances[start] = 0
    previous = {node["id"]: None for node in nodes}

    while heap:
        (distance, current) = heappop(heap)

        if current == end:
            path = []
            while previous[current] is not None:
                path.append(current)
                current = previous[current]
            path.append(start)
            return {"distance": distance, "path": path[::-1]}

        if current in visited:
            continue

        visited.add(current)

        for (neighbor, edge_distance) in adjacency_list[current]:
            distance_to_neighbor = distances[current] + edge_distance

            if distance_to_neighbor < distances[neighbor]:
                distances[neighbor] = distance_to_neighbor
                previous[neighbor] = current
                heappush(heap, (distance_to_neighbor, neighbor))

    return {"distance": None, "path": []}


roads={
  "graph": {
    "directed": False,
    "nodes": [
      { "id": 0 },
      { "id": 1 },
      { "id": 2 },
      { "id": 3 },
      {"id":4}
    ],
    "edges": [
      {
        "source": 0,
        "target": 1,
        "metadata": {
          "distance": 5
        }
      },
      {
        "source": 1,
        "target": 3,
        "metadata": {
          "distance": 9
        }
      },
      {
        "source": 3,
        "target": 2,
        "metadata": {
          "distance": 6
        }
      },
      {
        "source": 2,
        "target": 4,
        "metadata": {
          "distance": 3
        }
      },
      {
        "source": 4,
        "target": 3,
        "metadata": {
          "distance": 8
        },
      },
      {
       "source": 4,
       "target": 0,
       "metadata": {
         "distance": 2
       }
     }
    ]
  }
}
output={'distance': 5, 'path': [2, 4, 0]}
# print(navigate(roads, 2, 0))

assert navigate(roads, 2, 0)==output