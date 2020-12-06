from collections import defaultdict


def read_group_questions():
    f = open('in', 'r')
    groups = f.read().strip("\n").split("\n\n")
    return list(map(lambda x: x.split('\n'), groups))


def get_number_of_questions_ever_answered(groups):
    count = 0
    for group in groups:
        answered = {}
        for person in group:
            for question in person:
                answered[question] = True
        count += len(answered)
    return count


def get_number_of_questions_that_everyone_answered(groups):
    count = 0
    for group in groups:
        answered = defaultdict(int)
        people_count = len(group)
        for person in group:
            for question in person:
                answered[question] += 1
        for _, value in answered.items():
            if value == people_count:
                count += 1
    return count


def exec_part1(groups):
    return get_number_of_questions_ever_answered(groups)


def exec_part2(groups):
    return get_number_of_questions_that_everyone_answered(groups)


questions = read_group_questions()

# part 1
print(exec_part1(questions))

# part 2
print(exec_part2(questions))
