import functools 

def read_map():
    f = open('in', 'r')
    content = []
    for x in f:
        content.append(x.strip('\n'))
    return content 


def traverse_by_slope(slope):
    tree_map = read_map()
    right, down = slope
    x=0
    y=0
    count=0
    height=len(tree_map)
    width=len(tree_map[0])
    

    while y + down < height:
        x+=right;
        x = x % width
        y+=down
        if tree_map[y][x] == '#':
            count+=1

    return count


# part 1
print(traverse_by_slope([3, 1]))

# part 2
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

tree_count = map(traverse_by_slope, slopes)
product = functools.reduce(lambda a, b : a * b, tree_count)
print(product)
