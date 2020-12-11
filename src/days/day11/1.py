
def read_from_inputs():
    f = open('./in', 'r')
    return f.get_inputs().strip().split("\n")


EMPTY = "L"
OCCUPIED = "#"
FLOOR = '.'


SEATS = read_from_inputs()
SEAT_MAP_WIDTH = len(SEATS[0])
SEAT_MAP_HEIGHT = len(SEATS)


DIRECTIONS = [[-1, 0], [0, 1], [1, 0], [0, -1],
              [-1, 1], [1, 1], [-1, -1], [1, -1]]
DIR_LEN = len(DIRECTIONS)



def calc_dir_with_scalar(idx, scalar):
    x, y = DIRECTIONS[idx]
    return x * scalar, y * scalar


def is_valid_scalar(scalar):
    return scalar < SEAT_MAP_WIDTH and scalar < SEAT_MAP_HEIGHT


def is_valid_boundary(x, y):
    return 0 <= y < SEAT_MAP_HEIGHT and 0 <= x < SEAT_MAP_WIDTH


def calc_by_extended_seats(current):
    next = copy_from(current)
    for x in range(SEAT_MAP_WIDTH):
        for y in range(SEAT_MAP_HEIGHT):
            occupied_seats = 0
            for i in range(DIR_LEN):
                scalar = 1
                while is_valid_scalar(scalar):
                    dx, dy = calc_dir_with_scalar(i, scalar)
                    if not is_valid_boundary(x+dx, y+dy) or is_cell_empty(current, x+dx, y+dy):
                        break
                    if is_cell_floor(current, x+dx, y+dy):
                        scalar += 1
                    elif is_cell_occupied(current, x+dx, y+dy):
                        occupied_seats += 1
                        break
            update_cell_state(current, next, occupied_seats, x, y, 5)
    return next


def is_cell_occupied(map, x, y):
    return map[y][x] == OCCUPIED


def is_cell_empty(map, x, y):
    return map[y][x] == EMPTY


def is_cell_floor(map, x, y):
    return map[y][x] == FLOOR


def count_occupied_seats(rows):
    return sum([row.count(OCCUPIED) for row in rows])


def update_cell_state(current, next, occupied_seats, x, y, limit):
    if is_cell_empty(current, x, y) and occupied_seats == 0:
        next[y] = next[y][:x] + \
            OCCUPIED + next[y][x + 1:]
    elif is_cell_occupied(current, x, y) and occupied_seats >= limit:
        next[y] = next[y][:x] + EMPTY + next[y][x + 1:]


def copy_from(current_state):
    return [row for row in current_state]


def calc_by_adjacent_seats(current):
    next = copy_from(current)
    for x in range(SEAT_MAP_WIDTH):
        for y in range(SEAT_MAP_HEIGHT):
            occupied_seats = 0
            for dx, dy in DIRECTIONS:
                if is_valid_boundary(x+dx, y+dy) and is_cell_occupied(current, x+dx, y+dy):
                    occupied_seats += 1
            update_cell_state(current, next, occupied_seats, x, y, 4)
    return next


def perform(current, calc_next_state):
    while True:
        updated = calc_next_state(current)
        if current == updated:
            break
        current = updated
    return count_occupied_seats(current)


# part 1
print(perform(SEATS, calc_by_adjacent_seats))

# part 2
print(perform(SEATS, calc_by_extended_seats))
