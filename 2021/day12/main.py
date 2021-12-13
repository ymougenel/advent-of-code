#!/usr/bin/env python3
import time



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


def get_paths(graph, location, small_cave_twice="", visited=[], current_path=[], paths_done=[]):
    if not current_path:
        current_path = [location]
    else:
        current_path.append(location)

    if location == "end":
        paths_done.append(current_path)
        return paths_done

    if location.islower():
        if small_cave_twice == location:
            small_cave_twice = ""
        else:
            visited.append(location)

    children = graph[location]
    new_paths = []
    for child in children:
        if not child in visited:
            get_paths(graph, child, small_cave_twice, visited.copy(), current_path.copy(), paths_done)
            # if location.islower() and not small_cave_twice:
            #     get_paths(graph, child, location, visited.copy(), current_path.copy(), paths_done)
    return paths_done


if __name__ == '__main__':
    start_time = time.time()

    # Part 1
    # data = read_file("inputs/example1.txt")
    data = read_file("inputs/example2.txt")
    # data = read_file("inputs/example3.txt")
    data = read_file("inputs/part1.input")

    map = init_graph(data)

    # print(map)
    # print(len(get_paths(map, "start")))

    # Part 2

    # res = get_paths(map, "start")
    # print(res)
    # print(len(res))

    paths = []
    for node in map.keys():
        if node == "start":
            node_paths = get_paths(map, "start")
        if node == "end":
            node_paths = []
        elif node.islower():
            node_paths = get_paths(map, "start", node)
        else:
            node_paths = []
        for p in node_paths:
            if p not in paths:
                paths.append(p)
    print(len(paths))
    print("--- %s seconds ---" % (time.time() - start_time))
