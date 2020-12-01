#!/usr/bin/env python3


def read_file(fileName):
    inputFile = open(fileName, "r")
    data = inputFile.read().splitlines()
    inputFile.close()
    return data


def init_graph(chain):
    graph = {}
    for orbit in chain:
        A = orbit.split(")")[0]
        B = orbit.split(")")[1]
        if A not in graph.keys():
            graph[A] = [B]
        else:
            graph[A].append(B)
    return graph


def count_indirect_orbits(graph, current_element='COM', depth=0):
    if not current_element in graph.keys():
        return max(0, depth - 1)
    count = 0
    children = graph[current_element]
    for child in children:
        count += count_indirect_orbits(graph, child, depth + 1)
    return count + max(0, depth - 1)


def count_direct_orbits(graph):
    count = 0
    for key in graph.keys():
        count += len(graph[key])
    return count


def get_path(graph, current, destination):
    if current == destination:  # If found destination
        return [destination]
    elif not current in graph.keys():  # If dead end (graph leaf)
        return []

    for child in graph[current]:
        path = get_path(graph, child, destination)
        if path != []:  # Destination found among child
            return [current] + path
    return []  # Destination is not here


def get_minimum_transfer(graph, origin='COM', p1='SAN', p2='YOU'):
    # Trace 2 paths from graph origin to positions
    path1 = get_path(graph, origin, p1)
    path2 = get_path(graph, origin, p2)

    min_transfert = len(path1) + len(path2)
    # Look for intersections in paths
    for element in path1:
        if element in path2:
            transferts_p1_intersection = path1.index(p1) - path1.index(element) - 1
            transferts_p2_intersection = path2.index(p2) - path2.index(element) - 1
            min_transfert = min(min_transfert, transferts_p1_intersection + transferts_p2_intersection)
    return min_transfert


if __name__ == '__main__':
    chain = read_file("inputs/day6.input")
    # chain = read_file("inputs/day6_example.input")
    # chain = read_file("inputs/day6_example2.input")
    graph = init_graph(chain)

    c1 = count_direct_orbits(graph)
    c2 = count_indirect_orbits(graph)
    print(c1 + c2)

    print(get_minimum_transfer(graph))
