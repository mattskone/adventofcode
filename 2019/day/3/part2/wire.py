import sys


def get_vertices(path):
    steps = 0
    vertices = {}
    x, y = 0, 0
    for step in path:
        step_direction = step[0]
        step_size = int(step[1:])
        for i in range(1, step_size + 1):
            steps += 1
            if step_direction == 'U':
                y += 1
            elif step_direction == 'D':
                y -= 1
            elif step_direction == 'R':
                x += 1
            elif step_direction == 'L':
                x -= 1

            if x in vertices.keys():
                vertices[x].append((y, steps))
            else:
                vertices[x] = [((y, steps))]

    return vertices


def get_intersection_distances(vertices1, vertices2):
    intersections = []
    for x in vertices1.keys():
        if x in vertices2.keys():
            for y1, steps1 in vertices1[x]:
                for y2, steps2 in vertices2[x]:
                    if y1 == y2:
                        intersections.append(steps1 + steps2)
        else:
            continue

    return intersections


def main(wire1, wire2):
    vertices1 = get_vertices(wire1)
    vertices2 = get_vertices(wire2)
    distances = get_intersection_distances(vertices1, vertices2)

    return min(distances)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        wire1, wire2 = f.readlines()

    wire1 = wire1.replace('\n', '')
    wire1 = wire1.split(',')
    wire2 = wire2.replace('\n', '')
    wire2 = wire2.split(',')

    print(main(wire1, wire2))
