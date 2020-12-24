cups=[3,9,8,2,5,4,7,1,6]

def get_pick_range(current, n):
    return [(current + i + n ) % n  for i in range(1, 4)]


def mod_n(v):
    n = len(cups)
    return (v + n ) % n

def get_destination_idx(current_idx, cups, picked_idxs):
    d={
        cups[i]: i for i in range(len(cups))
      }
    found = False
    smallest_idx = d[min(cups)]
    target_val = cups[current_idx] - 1
    if target_val == 0:
        return find_highest(cups, [current_idx] + picked_idxs)
    target_idx = d[target_val]
    while not found:
        if target_idx in picked_idxs:
            if target_idx == smallest_idx:
                return find_highest(cups, [current_idx] + picked_idxs)
            else:
                target_val = mod_n(target_val-1)
                if target_val == 0:
                    return find_highest(cups, [current_idx] + picked_idxs)
                target_idx = d[mod_n(target_val)]
                # continue next round
        else:
            return target_idx



def find_highest(cups, exclude):
    x = max([cups[i] for i in range(len(cups)) if i not in exclude])
    return cups.index(x)

def arrange_order(current, des, picked, cups):
    copied =[]
    for i in range(len(cups)):
        if i not in picked:
            copied.append(cups[i])
    goto = copied.index(cups[des])
    old = copied[:goto+1] + [cups[p] for p in picked] + copied[goto+1:]
    idx = old.index(cups[current])

    if idx > current:
        diff = idx - current
        old = old[diff:] + old[:diff]
    elif idx < current:
        diff = current - idx
        old = old[-diff:] + old[:-diff]

    return old



def exec_part_1(cups, moves):
    i = 0
    current_idx=0
    n = len(cups)
    while i < moves:
        picked = get_pick_range(current_idx, len(cups))
        des_idx = get_destination_idx(current_idx, cups, picked)
        cups = arrange_order(current_idx, des_idx, picked, cups)
        current_idx = (current_idx + 1 + n )% n
        i+=1
    one_i = cups.index(1)
    return ''.join([str(x) for x in cups[one_i+1:] + cups[:one_i+1]])[:-1]



ans = exec_part_1(cups, 100)
print(ans)
