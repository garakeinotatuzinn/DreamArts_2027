import sys
graph = {}
stations = set()

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    start, end, distance = map(str.strip, line.split(","))

    start = int(start)
    end = int(end)
    distance = float(distance)

    if start not in graph:
        graph[start] = []
    graph[start].append((end, distance))

    if end not in graph:
        graph[end] = []
    graph[end].append((start, distance))

    stations.add(start)
    stations.add(end)

max_distance = 0
max_route = []


def brute_force(current, distance, route, visited):
    global max_distance, max_route

    if distance > max_distance:
        max_distance = distance
        max_route = route.copy()

    for next_station, next_distance in graph[current]:
        if next_station not in visited:
            visited.add(next_station)
            route.append(next_station)

            brute_force(
                next_station,
                distance + next_distance,
                route,
                visited
            )

            route.pop()
            visited.remove(next_station)


for start in stations:
    brute_force(
        start,
        0,
        [start],
        {start}
    )

for station in max_route:
    print(station)