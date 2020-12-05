
COLUMN_SIZE = 8
ROW_SIZE=128


def read_seats():
    f = open('in', 'r')
    return f.read().strip('\n').split("\n")

def binary_search(seat_letters, low, high):
    lo = low
    hi = high
    max_len = len(seat_letters)
    mid = lo + (( hi - lo) // 2)
    i = 0
    while lo <= hi and i < max_len:
        if seat_letters[i] in 'FL':
            hi = mid 
        elif seat_letters[i] in 'BR':
            lo = mid + 1
        i+=1
        if  lo <= hi:
            mid = lo + (( hi - lo) // 2)
    return mid


def calc_seat_row(seat):
    return binary_search(seat[0:COLUMN_SIZE-1], 0, ROW_SIZE-1)


def calc_seat_column(seat):
    return binary_search(seat[COLUMN_SIZE-1:], 0, COLUMN_SIZE-1)


def calc_seat_id(seat):
    row = calc_seat_row(seat)
    column = calc_seat_column(seat)
    return row * COLUMN_SIZE + column


def highest_row(seats):
    return max([calc_seat_row(seat) for seat in seats])

def get_all_seat_ids(seats):
    return [calc_seat_id(seat) for seat in seats]


def find_my_seat_id(seats):
    ids = sorted(get_all_seat_ids(seats))
    for i in range(1, len(ids)):
        if ids[i-1] != ids[i] - 1:
            return ids[i] - 1

def find_highest_seat_id(seats):
    return max(get_all_seat_ids(seats))

seats = read_seats()


# part 1
print(find_highest_seat_id(seats))

# part 2
print(find_my_seat_id(seats))
