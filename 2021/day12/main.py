#!/usr/bin/env python3


def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def init_graph(chain):
    graph = {}
    for cave_path in chain:
        A = cave_path.split("-")[0]
        B = cave_path.split("-")[1]
        if A not in graph.keys():
            graph[A] = [B]
        else:
            graph[A].append(B)
        if B not in graph.keys():
            graph[B] = [A]
        else:
            graph[B].append(A)
    return graph


def get_paths(graph, location, visited=[], current_path=[], paths_done=[]):
    if not current_path:
        current_path = [location]
    else:
        current_path.append(location)

    if location == "end":
        paths_done.append(current_path)
        return paths_done

    if location.islower():
        visited.append(location)

    children = graph[location]
    new_paths = []
    for child in children:
        if not child in visited:
            get_paths(graph, child, visited.copy(), current_path.copy(), paths_done)
    return paths_done


if __name__ == '__main__':
    # Part 1
    data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    data = read_file("inputs/example3.txt")
    data = read_file("inputs/part1.input")

    map = init_graph(data)

    print(map)
    paths = get_paths(map, "start")
    print(paths)
    print(len(paths))
    # Part 2
    # data = read_file("inputs/example2.txt")
