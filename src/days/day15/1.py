from collections import defaultdict
starting_numbers = [0,8,15,2,12,1,4]

def calc_recent(turns):
    t1, t2 = turns
    return abs(t1 - t2)

def exec_part_1(n):
    turn = 0
    i=0
    spoken_in_turns = defaultdict(list)
    spoken_count=defaultdict(int)
    most_recent_spoken=None
    ll = len(starting_numbers)
    while turn < n:
        print(turn)
        turn += 1
        # starting number first
        if i < ll:
            most_recent_spoken = starting_numbers[i]
            record_recent_spoken(spoken_in_turns, most_recent_spoken, turn)
            i+=1
            continue
        elif len(spoken_in_turns[most_recent_spoken]) == 1:
            most_recent_spoken = 0
            record_recent_spoken(spoken_in_turns, most_recent_spoken, turn)

        elif len(spoken_in_turns[most_recent_spoken]) > 1:
            most_recent_spoken = calc_recent(spoken_in_turns[most_recent_spoken])
            record_recent_spoken(spoken_in_turns, most_recent_spoken, turn)

    print(most_recent_spoken)


# def record_spoken(most_recent_spoken, spoken_in_turns, turn):
    # increase_spoken_count(most_recent_spoken, spoken_count)


# def increase_spoken_count(most_recent_spoken, spoken_count):
#     spoken_count[most_recent_spoken] += 1
#

def record_recent_spoken(spoken_in_turns, most_recent_spoken, turn):
    if most_recent_spoken in spoken_in_turns:
        spoken_in_turns[most_recent_spoken] = [spoken_in_turns[most_recent_spoken][-1], turn]
    else:
        spoken_in_turns[most_recent_spoken] = [turn]
    return spoken_in_turns


print(exec_part_1(2020))


# exec part 2 take a long time...
# need to find a more efficient way
print(exec_part_1(30000000))

