def read_instructions():
    f = open('./in', 'r')
    content = [item for item in f.read().strip().split("\n") ]
    f.close()
    return content


def normalize_inst(inst):
    a, b = inst.split( )
    return a, int(b)

def perform_opt(inst, cur, acc):
    opt, val = normalize_inst(inst)
    return {
        'nop': lambda c, a : (c+1, a),
        'jmp': lambda c, a : (c+val, a),
        'acc': lambda c, a : (c+1, a+val),
    }[opt](cur, acc)

def run_programming(instructions):
    cur, accumulator, seen= 0, 0, set()
    while cur not in seen and cur < len(instructions):
        seen.add(cur)
        cur, accumulator = perform_opt(instructions[cur], cur, accumulator)
    return accumulator, cur == len(instructions)

inst = read_instructions()

swap_opts={
    'jmp': 'nop',
    'nop': 'jmp',
}

def get_swap_opt(opt):
    return swap_opts[opt]

def replaced(opt, instruction):
    return instruction.replace(opt, get_swap_opt(opt))

def exec_part2():
    instructions = read_instructions()
    print(instructions)
    n=len(instructions)
    for i in range(0, n):
        opt, _ = normalize_inst(instructions[i])
        if opt not in swap_opts:
            cur = instructions[i]
            instructions[i] = replaced(opt, cur)
            acc, correct = run_programming(instructions)
            if correct:
                return acc
            else:
                instructions[i] = cur

exec_part2()
