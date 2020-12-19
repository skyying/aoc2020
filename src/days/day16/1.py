from operator import itemgetter, attrgetter

def parse_range(ary):
    ans = []
    for x in ary:
        x1, x2 = x.split("-")
        ans.append((int(x1), int(x2)))
    return ans

def parsed_t2(tickets):
    tt = tickets.split("\n")[1:]
    ans = []
    for t in tt:
        ans.append([int(x) for x in t.split(',')])
    return ans

def range_rule_by_row(rules_str):
    rules = {}
    for i, rule in enumerate(rules_str):
        name, detail = rule.split(": ")
        r1, r2 = detail.split(" or ")
        rules[name]=parse_range([r1, r2]) + [i]
    return rules

def read_input():
    f = open('./in', 'r')
    cc = f.read().strip().split("\n\n")
    ran, t1, t2 = cc
    rr = ran.split('\n')
    valid_range=[]
    for r in rr:
        r1, r2 = r.split(": ")[1].split(" or ")
        parsed_range = parse_range([r1, r2])
        for p in parsed_range:
            valid_range.append(p)
    at1 = [int(x) for x in t1.strip().split('\n')[1].split(",")]
    at2 = parsed_t2(t2)
    rules = range_rule_by_row(rr)
    return valid_range, at1, at2, rules

def parse_valid_range(ran):
    aa = sorted(ran, key=lambda x: x[0])
    stack = [aa[0]]

    for i in range(1, len(aa)):
        s1, e1 = stack.pop()
        s2, e2 = aa[i]
        if e1 >= s2 or e1 + 1 == s2:
            stack.append((s1, e2))
        else:
            stack.append((s1, e1))
            stack.append(aa[i])
    return stack

def exec_part1(valid_ranges, nearby_tickets):
    valid_range_list = parse_valid_range(valid_ranges)
    error_rate = 0
    valid_tickets=[]
    for ticket in nearby_tickets:
        is_all_field_valid=True
        for field in ticket:
            is_field_valid = False
            for valid_range in valid_range_list:
                start, end = valid_range
                if start<=field<=end:
                    is_field_valid=True
                    break
                else:
                    is_all_field_valid=False
            if not is_field_valid:
                error_rate+=field
        if is_all_field_valid:
            valid_tickets.append(ticket)

    return error_rate, valid_tickets

def validate_range(current, rule):
    start, end, _ = rule
    ss, se = start
    es, ee = end
    if current[0] < ss or current[-1] > ee:
        return False
    for x in current:
        if se < x < es:
            return False
    return True

def reversed_tickets_by_fields(tickets):
    reversed = []
    for i in range(len(tickets[0])):
        reversed.append([])
        for j in range(len(tickets)):
            value = tickets[j][i]
            reversed[i].append(value)
        reversed[i] = sorted(reversed[i])
    return reversed

def calc_matched_filed_name_in_ticket_index(rules, fields_in_tickets):
    matched = {}
    for name, rule in rules.items():
        for fi in range(len(fields_in_tickets)):
            is_valid = validate_range(fields_in_tickets[fi], rule)
            if is_valid:
                if name in matched:
                    matched[name] = matched[name] + [fi]
                else:
                    matched[name] = [fi]
    return matched


def exec_part2(rules, my_ticket, valid_tickets):
    reversed = reversed_tickets_by_fields(valid_tickets)
    matched = calc_matched_filed_name_in_ticket_index(rules, reversed)
    sorted_matched = sorted(matched, key=lambda k: len(matched[k]))
    valid_field_index = {}
    for i, name in enumerate(sorted_matched):
        assert len(matched[name]) == 1
        valid_field_index[name] = matched[name][0]
        to_remove=valid_field_index[name]
        for other_name in sorted_matched[i+1:]:
            matched[other_name].remove(to_remove)
    ans = 1
    for name, i in valid_field_index.items():
        if name.startswith('departure'):
            ans = ans*my_ticket[i]
    return ans

valid_range, my_ticket, nearby_tickets, range_rules = read_input()
error_rate, valid_tickets = exec_part1(valid_range, nearby_tickets)
print('Part 1 => ', error_rate)
ans = exec_part2(range_rules, my_ticket,  valid_tickets)
print('Part 2 => ', ans)
