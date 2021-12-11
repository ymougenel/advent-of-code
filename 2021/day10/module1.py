def read_file(file_name):
    with open(file_name) as input_file:
        return [line for line in input_file.read().splitlines()]


def get_error_count(line):
    opened = []

    for c in line:
        if c in "{(<[":
            opened.append(c)
        else:
            last_opened = opened.pop()
            if c == ">" and last_opened != "<":
                return 25137
            if c == "}" and last_opened != "{":
                return 1197
            if c == ")" and last_opened != "(":
                return 3
            if c == "]" and last_opened != "[":
                return 57
    return 0


def get_imcomplete_count(line):
    opened = []
    for c in line:
        if c in "{(<[":
            opened.append(c)
        else:
            last_opened = opened.pop()
    count = 0
    opened.reverse()
    for c in opened:
        count = count * 5
        if c == "(":
            count += 1
        if c == "[":
            count += 2
        if c == "{":
            count += 3
        if c == "<":
            count += 4
    return count


if __name__ == '__main__':
    content = read_file("inputs/part1.example.txt")
    content = read_file("inputs/input1.txt")

    # Part 1
    # print(sum([get_error_count(line) for line in content]))

    #  Part 2
    valid_lines = [line for line in content if get_error_count(line) == 0]
    scores = [get_imcomplete_count(line) for line in valid_lines]
    list.sort(scores)
    print(scores[len(scores) // 2])
