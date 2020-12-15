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
    while turn < n:
        turn += 1
        # starting number first
        if i < len(starting_numbers):
            most_recent_spoken = starting_numbers[i]
            record_spoken(most_recent_spoken, spoken_count, spoken_in_turns, turn)
            i+=1
            continue
        elif spoken_count[most_recent_spoken] == 1:
            most_recent_spoken = 0
            record_spoken(most_recent_spoken, spoken_count, spoken_in_turns, turn)

        elif spoken_count[most_recent_spoken] > 1:
            most_recent_spoken = calc_recent(spoken_in_turns[most_recent_spoken])
            record_spoken(most_recent_spoken, spoken_count, spoken_in_turns, turn)

        print(most_recent_spoken)


def record_spoken(most_recent_spoken, spoken_count, spoken_in_turns, turn):
    record_recent_spoken(spoken_in_turns, most_recent_spoken, turn)
    increase_spoken_count(most_recent_spoken, spoken_count)


def increase_spoken_count(most_recent_spoken, spoken_count):
    spoken_count[most_recent_spoken] += 1


def record_recent_spoken(spoken_in_turns, most_recent_spoken, turn):
    spoken_in_turns[most_recent_spoken].append(turn)
    while len(spoken_in_turns[most_recent_spoken]) > 2:
        spoken_in_turns[most_recent_spoken].pop(0)
    return spoken_in_turns


exec_part_1(2020)

