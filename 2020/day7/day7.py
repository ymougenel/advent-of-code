#!/usr/bin/env python3

def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


parent_bag = re.compile('^(\w+ \w+)')
parent_content = re.compile('(\d) (\w+ \w+)')

def init_tree(rules):
    graph = {}

    for rule in rules:
        bag = parent_bag.search(rule).group()
        contents = parent_bag.search(rule).group()

        bag = rule.split("bags contain")[0].strip()
        contents = rule.split("bags contain")[1] \
            .replace("bags", "") \
            .replace("bag", "") \
            .split(',')
        dependencies = []
        for content in contents:
            content = content.strip()
            count_value = 0 if content[0] == 'n' else int(content[0])
            content = content.replace('.', '').strip()

            # dependencies.append(content[2:])
            dependencies.append((count_value, content[2:]))
        if bag not in graph.keys():
            graph[bag] = dependencies
        else:
            graph[bag].append(dependencies)
    return graph


def find_containing(graph, bag):
    containing = []
    for node in graph.keys():
        if node != bag and contains(graph, graph.keys(), node, bag):
            containing.append(node)

    return containing


def contains(graph, keys, candidate_bag, target_bag):
    if candidate_bag not in keys:
        return False
    for dep in graph[candidate_bag]:
        if dep[1] == target_bag:
            return True
        elif contains(graph, keys, dep[1], target_bag):
            return True
    return False


def count_bags(tree, root_bag):
    total = 0
    for bag_count,bags_contained in tree[root_bag]:
        # Leaf, termination
        if bag_count == 0:
            return 0
        # Recursion on all the contained bag
        else:
            total += bag_count + bag_count * count_bags(tree, bags_contained)
    return total


if __name__ == '__main__':
    # rules = read_file("inputs/part1.example")
    # rules = read_file("inputs/part2.example")
    rules = read_file("inputs/part1.input")
    tree = init_tree(rules)
    # print(graph)
    print("Part1: " + str(len(find_containing(tree, "shiny gold"))))
    print("Part2: " + str(count_bags(tree, "shiny gold")))
