def read_instructions():
    f = open('./in', 'r')
    return [ (s[:1], int(s[1:])) for s in f.read().strip().split('\n')]

def move_east(x, y, steps):
    return x + steps, y

def move_west(x, y, steps):
    return x - steps, y

def move_north(x, y, steps):
    return x, y + steps

def move_south(x, y, steps):
    return x, y - steps

move_directions = {
    'E': move_east,
    'W': move_west,
    'N': move_north,
    'S': move_south,
}

DIRECTIONS=['E', 'N', 'W', 'S']

def move_ship(sx, sy, wx, wy, scalar):
    return sx + (wx*scalar), sy + (wy*scalar)

def move_waypoint(x, y, instruction):
    dir, steps = instruction
    x, y = move_directions[dir](x, y, steps)
    return x, y

def rotate_clockwise_n_degree(x, y, degrees):
    if degrees == 0:
        return x, y
    if degrees == 90:
        return y, -x
    if degrees == 180:
        return -x, -y
    if degrees == 270:
        return -y, x

def rotate_counter_clockwise_n_degree(x, y, degrees):
    if degrees == 0:
        return x, y
    if degrees == 90:
        return -y, x
    if degrees == 180:
        return -x, -y
    if degrees == 270:
        return y, -x


def part_2(instructions):
    sx, sy = 0, 0
    wx, wy = 10, 1
    for instruction in instructions:
        dir, steps = instruction
        if dir in DIRECTIONS:
            wx, wy = move_waypoint(wx, wy, instruction)
        if dir in 'F':
            sx, sy = move_ship(sx, sy, wx, wy, steps)
        if dir == 'R':
            wx, wy = rotate_clockwise_n_degree(wx, wy, steps)
        if dir in 'L':
            wx, wy = rotate_counter_clockwise_n_degree(wx, wy, steps)
    return abs(sx) + abs(sy)

print(part_2(read_instructions()))
