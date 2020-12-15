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
    cur_idx, accumulator, seen= 0, 0, set()
    while cur_idx not in seen and cur_idx < len(instructions):
        seen.add(cur_idx)
        cur_idx, accumulator = perform_opt(instructions[cur_idx], cur_idx, accumulator)
    return accumulator, cur_idx == len(instructions)

def get_swap_opt(opt):
    return {
        'jmp': 'nop',
        'nop': 'jmp',
        'acc': 'acc',
    }[opt]

def swapped_opt(opt, instruction):
    return instruction.replace(opt, get_swap_opt(opt))

def exec_part1(instructions):
    acc, correct = run_programming(instructions)
    return acc

def exec_part2(instructions):
    n=len(instructions)
    for i in range(n):
        opt, _ = normalize_inst(instructions[i])
        current_instruction = instructions[i]
        instructions[i] = swapped_opt(opt, current_instruction)
        acc, correct = run_programming(instructions)
        if correct:
            return acc
        else:
            instructions[i] = current_instruction
    return None


instruction_list=read_instructions()

print("Part 1:", exec_part1(instruction_list))
print("Part 2:", exec_part2(instruction_list))
