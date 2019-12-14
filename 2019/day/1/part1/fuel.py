'''
Solution to https://adventofcode.com/2019/day/1

Run with full or relative path to input file.  Eg/

$ python fuel.py /tmp/input.txt

Input file should contain contents of https://adventofcode.com/2019/day/1/input
'''


import sys


def clean_input(mass):
    mass = mass.replace('\n', '')
    try:
        return int(mass)
    except ValueError:
        return 0


def compute_fuel_requirement(mass):
    return max([mass / 3 - 2, 0])


def main():
    with open(sys.argv[1]) as f:
        masses = map(clean_input, f.readlines())
    fuel_requirements = map(compute_fuel_requirement, masses)

    return sum(fuel_requirements)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Expected one argument: path to input file')
        sys.exit(1)
    print(main())

