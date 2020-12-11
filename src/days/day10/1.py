from collections import defaultdict

def get_adapter_in_bags():
    f = open('./in', 'r')
    return sorted(list(map(lambda x: int(x), f.read().strip().split("\n"))))

def get_adapters():
    adapters_in_bags=get_adapter_in_bags()
    return [0] + adapters_in_bags + [max(adapters_in_bags) + 3]


def product_of_differences():
    adapters = get_adapters()
    difference_occurrence=defaultdict(int)
    for i in range(1, len(adapters)):
        diff=adapters[i] - adapters[i-1]
        difference_occurrence[diff]+=1
    return difference_occurrence[1] * difference_occurrence[3]

# part 1
print(product_of_differences())

# part 2


