import sys


def solve(opcodes):
    for i in range(0, len(opcodes), 4):
        if opcodes[i] == 1:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] + opcodes[opcodes[i + 2]]
        elif opcodes[i] == 2:
            opcodes[opcodes[i + 3]] = opcodes[opcodes[i + 1]] * opcodes[opcodes[i + 2]]
        elif opcodes[i] == 99:
            return opcodes
        else:
            raise ValueError('Invalid opcode {0} at position {1}'.format(opcodes[i], i))


def main(noun, verb):
    with open(sys.argv[1]) as f:
        opcodes = f.read()
    opcodes = opcodes.replace('\n', '')
    opcodes = opcodes.split(',')
    opcodes = list(map(int, opcodes))

    opcodes[1] = int(noun)
    opcodes[2] = int(verb)

    return solve(opcodes)


if __name__ == '__main__':
    # NOTE: Solution is 25, 52 (trial and error was predictable and fast)
    if len(sys.argv) != 4:
        print('Expected three arguments: path to input file, noun, and verb')
        sys.exit(1)
    print(main(sys.argv[2], sys.argv[3])[0])
