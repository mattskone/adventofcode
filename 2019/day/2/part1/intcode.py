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


def main():
    with open(sys.argv[1]) as f:
        opcodes = f.read()
    opcodes = opcodes.replace('\n', '')
    opcodes = opcodes.split(',')
    opcodes = list(map(int, opcodes))

    opcodes[1] = 12
    opcodes[2] = 2

    return solve(opcodes)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Expected one argument: path to input file')
        sys.exit(1)
    print(main())
