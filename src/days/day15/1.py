import time
starting_numbers = [0,8,15,2,12,1,4]

def calc_recent(turns):
    t1, t2 = turns
    return abs(t1 - t2)

def exec_part_1(n):
    spoken_in_turns = {}
    spoken_set=set()
    turn=0
    for i in range(len(starting_numbers)-1):
        spoken_set.add(starting_numbers[i])
        spoken_in_turns[starting_numbers[i]]=i+1
    last_spoken = starting_numbers[-1]
    turn += len(starting_numbers)
    while turn < n:
        if last_spoken not in spoken_set:
            tmp=0
        else:
            tmp= turn - spoken_in_turns[last_spoken]

        spoken_in_turns[last_spoken] = turn
        spoken_set.add(last_spoken)

        last_spoken=tmp
        turn+=1
    return last_spoken

print(exec_part_1(2020))

start_time = time.time()
print(exec_part_1(30000000))
print(time.time() - start_time)

