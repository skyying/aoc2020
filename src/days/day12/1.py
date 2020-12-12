
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

def move_forward(x, y, steps, dir_idx):
    dir=get_current_direction(dir_idx)
    return move_directions[dir](x, y, steps)

def turn_right(old, steps):
    idx=(old+4-steps)%4
    return idx

def turn_left(old, steps):
    idx=(old+steps)%4
    return idx

move_directions = {
    'E': move_east,
    'W': move_west,
    'N': move_north,
    'S': move_south,
    'R': turn_right,
    'L': turn_left
}

DIRECTIONS=['E', 'N', 'W', 'S']

def get_current_direction(idx):
    return DIRECTIONS[idx % 4]

def move(x, y, dir_idx, instruction):
    dir, steps = instruction
    if dir in DIRECTIONS:
        x, y = move_directions[dir](x, y, steps)
        return x, y, dir_idx
    if dir == 'F':
        x, y = move_forward(x, y, steps, dir_idx)
        return x, y, dir_idx
    if dir in 'RL':
        return x, y, move_directions[dir](dir_idx, steps // 90)
    return None, None, None


def exec_part1(instructions):
    x, y, direction_idx = 0, 0, 0
    for instruction in instructions:
        x, y, direction_idx = move(x, y, direction_idx, instruction)
    return abs(x) + abs(y)

instructions_list=read_instructions()
print(exec_part1(instructions_list))
