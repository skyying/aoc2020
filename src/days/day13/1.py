import math


def read_input():
    f = open('./in', 'r')
    timestamp, bus_list = f.read().strip().split("\n")
    buses =  filter(lambda  x : x != 'x', bus_list.split(","))
    return int(timestamp), [ int(b) for b in buses]


def read_input2():
    f = open('./in', 'r')
    timestamp, bus_list = f.read().strip().split("\n")
    return int(timestamp), bus_list.split(",")

def part_1(timestamp, buses):
    waiting_time = list(map(lambda b: math.ceil(timestamp / b) * b - timestamp, buses))
    output = float('inf')
    product=0
    for i in range(len(waiting_time)):
        if waiting_time[i] < output:
            output = waiting_time[i]
            product = (waiting_time[i]) * buses[i]
    return product

def mapBus(b):
    return 0 if b == 'x' else int(b)

def not_position(scalar, buses, max_bus_id):
    earliest = max_bus_id * scalar
    print(earliest)
    for bus in buses:
        offset, bus_id = bus
        if offset == 0:
            continue
        if bus_id * scalar != offset + earliest:
            return True
    return False
t1, b1 = read_input()
print(part_1(t1, b1))
