def parse_input():
    f = open('in', 'r')
    content = []
    for x in f:
        limit, c, pw = x.strip('\n').split(" ")
        low, hi = limit.split('-')
        d = [int(low), int(hi), c.strip(':'), pw]
        content.append(d)
    return content


def get_valid_password_count_by_boundaries_correctness(passwords):
    count = 0
    for p in passwords:
        lookup = {}
        low, hi, c, pw = p
        for pc in pw:
            if pc in lookup:
                lookup[pc] += 1
            else:
                lookup[pc] = 1

        if c in lookup:
            if low <= lookup[c] <= hi:
                count += 1

    return count


def get_valid_password_count_by_position_correctness(passwords):
    count = 0
    for p in passwords:
        p1, p2, c, pw = p
        if pw[p1-1] == c and pw[p2-1] != c:
            count += 1
        elif pw[p1-1] != c and pw[p2-1] == c:
            count += 1
    return count


def exec_part1(input):
    return get_valid_password_count_by_boundaries_correctness(inputs)


def exec_part2(input):
    return get_valid_password_count_by_position_correctness(inputs)


inputs = parse_input()


# part 1
print(exec_part1(inputs))


# part 2
print(exec_part2(inputs))
