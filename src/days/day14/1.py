import re
from collections import defaultdict

get_bin = lambda x: format(x, '036b')

def read_input():
    f = open('./in', 'r')
    return f.read().strip().split('\n')


def calc_updated_value(mask, value):
    bin_value = get_bin(int(value))
    for i in range(len(bin_value)):
        if mask[i] != 'X':
            bin_value = bin_value[:i] + mask[i] + bin_value[i+1:]
    return int(bin_value, 2)


def perform_update(storage, mask, address, value):
    updated_value = calc_updated_value(mask, value)
    storage[address]=updated_value
    return storage


def part_1():
    storage=defaultdict(int)
    mask=''
    for line in lines:
        left, right = line.split(" = ")
        if left == 'mask':
            mask = right
        else:
            left = left.replace('mem[', '')
            address = left.replace(']', '')
            value = right
            storage = perform_update(storage, mask, address, value)
    return sum([x for x in storage.values()])




lines = read_input()
print(part_1())

