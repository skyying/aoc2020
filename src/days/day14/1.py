import re
from collections import defaultdict
import itertools

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


def format_address_with_mask(address, mask):
    address_list = list(address)
    for i in range(len(mask)):
        if mask[i] in '1X':
            address_list[i] = mask[i]
    return ''.join(address_list)


def calc_address(combination, address):
    address_str = list(address)
    m = len(address)
    j = -1
    for i in range(m):
        if address_str[i] == 'X':
            j+=1
            address_str[i] = combination[j]
    return int(''.join(address_str), 2)

def calc_updated_addresses(mask, address):
    # will return 0XX00 format
    b_address = format_address_with_mask(get_bin(address),mask)
    n = b_address.count('X')
    combinations = list(itertools.product("01", repeat=n))
    return [calc_address(cmb, b_address) for cmb in combinations]


def perform_update_v2(storage, mask, address, value):
    updated_addresses = calc_updated_addresses(mask, int(address))
    for address in updated_addresses:
        storage[address] = int(value)
    return storage


def exec_part_1():
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


def exec_part_2():
    """
    If the bitmask bit is 0, the corresponding memory address bit is unchanged.
    If the bitmask bit is 1, the corresponding memory address bit is overwritten with 1.
    If the bitmask bit is X, the corresponding memory address bit is floating.
    :return:
    """
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
            storage = perform_update_v2(storage, mask, address, value)
    return sum([x for x in storage.values()])

lines = read_input()
print(exec_part_1())
print(exec_part_2())
