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


if __name__ == '__main__':
    chain = read_file("inputs/day6.input")
    # chain = read_file("inputs/day6_example.input")
    graph = init_graph(chain)
    c1 = count_direct_orbits(graph)
    c2 = count_indirect_orbits(graph)
    print(c1 + c2)
