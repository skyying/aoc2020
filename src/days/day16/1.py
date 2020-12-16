
# class: 1-3 or 5-7
# row: 6-11 or 33-44
# seat: 13-40 or 45-50
#
# your ticket:
# 7,1,14
#
# nearby tickets:
# 7,3,47
# 40,4,50
# 55,2,20
# 38,6,12


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
        print(t)
        ans.append([int(x) for x in t.split(',')])
    return ans


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
    print(at1)
    return valid_range, at1, at2

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




def exec_part1(valid_range, my_tickets, nearby_tickets):
    ran = parse_valid_range(valid_range)
    ss = 0
    for ticket in nearby_tickets:
        for t in ticket:
            is_valid= False
            for r in ran:
                s, e = r
                if s<=t<=e:
                    is_valid=True
                    break
            if not is_valid:
                ss+=t

    print(ss)
    return ss




a, b, c = read_input()
exec_part1(a, b, c)
