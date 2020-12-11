
def two_entries(nums, target):
    seen = {}
    for i in nums:
        if (target - i) in seen:
            return i * (target - i)
        else:
            seen[i] = True
    return None


def get_inputs():
    f = open('./in', 'r')
    return [int(n) for n in f.read().strip().split("\n")]


def calc_first_number_of_not_meet_sum_of_pre_range(preamble_range, digits):
    for i in range(preamble_range, len(digits)):
        nums = digits[i - preamble_range: i]
        if not two_entries(nums, digits[i]):
            return digits[i]


def contagious_sum(n, digits):
    left=0
    right=0
    sum=digits[left]
    while sum != n and left <= right < len(digits):
        if sum < n:
            right+=1
            sum+=digits[right]
        else:
            sum-=digits[left]
            left+=1

        if sum == n and right - left > 1:
            print(digits[left], digits[right])

    mx=max(digits[left:right+1])
    mi=min(digits[left:right+1])
    return mx + mi


digits=get_inputs()

PREAMBLE_RANGE=25
first_number = calc_first_number_of_not_meet_sum_of_pre_range(PREAMBLE_RANGE, digits)

# part 1
print(first_number)

# part 2
print(contagious_sum(first_number, digits))


