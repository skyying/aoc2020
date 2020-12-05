
def read_file():
    f = open('in', 'r')
    content = []
    for x in f:
        content.append(x.strip('\n'))
    return content


def two_entries(nums, target):
    seen = {}
    for n in nums:
        if (target - n) in seen:
            return n * (target - n)
        else:
            seen[n] = True
    return None


def three_entries(nums, target):
    for i in range(0, len(nums)):
        remaining = target - nums[i]
        matched = two_entries(nums[i+1: len(nums)], remaining)
        if matched != None:
            return matched * nums[i]
    return -1


def exec_part1(nums):
    return two_entries(nums, 2020)


def exec_part2(nums):
    return three_entries(nums, 2020)


# input
nums = list(map(int, read_file()))


# part 1
print(exec_part1(nums))


# part 2
print(exec_part2(nums))
