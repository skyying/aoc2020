from collections import defaultdict
import functools


end_colors={}
def parse_line(line):
    """
    :param "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags"
    :return (root_color, [(child_color_1, count), (child_color_2, count)]
    """
    root_str, children_str = line.split("contain")
    root_color=root_str.strip()[:-5]
    if 'contain no other bags' in line:
        # -5 means remove ' bags', we only need color name
        end_colors[root_color]=True
        return root_color, []

    split_children = map(lambda x: x.split()[0:-1],children_str.split(","))
    formatted = list(map(lambda x: (' '.join(x[1:]), int(x[0].strip())),split_children))
    return root_color, formatted

def read_bags():
    f = open('in', 'r')
    return list(map(parse_line, f.read().strip("\n").split("\n")))

def build_graph(relations):
    graph={}
    for relation in relations:
        set={}
        root, children = relation
        for child in children:
            color, count=child
            set[color]=count
        graph[root]=set
    return graph

def bag_contain_target_color(graph, bag, target_color):
    if target_color in bag:
        return True
    return any([bag_contain_target_color(graph, graph[k], target_color) for k in bag])


def get_expanded_bags():
    expaned={}
    for k, v in graph.items():
        children=[]
        for xk, xv in v.items():
            children+=[xk for i in range(0, xv)]
        expaned[k]=children
    return expaned

def count_bags(target_color, expanded):
    if target_color in end_colors:
        return 0
    remaining=[]
    for color in expanded[target_color]:
        remaining.append(count_bags(color, expanded))
    return sum(remaining)+len(expanded[target_color])

bags=read_bags()
graph=build_graph(bags)
expanded_bags=get_expanded_bags()

def exec_part1():
    res = sum([bag_contain_target_color(graph, bag, 'shiny gold') for type, bag in graph.items()])
    print(res)

def exec_part2():
    print(count_bags('shiny gold', expanded_bags))


exec_part1()
exec_part2()
