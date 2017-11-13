
import sys

def main(argv):
    filename = argv[0]

    with open(filename, 'r') as fileptr:
        input_txt = fileptr.readlines()[0]
        # ^ I happen to know that there is only one line here

    dirs = [x.strip().rstrip() for x in input_txt.split(',')]

    x = 0
    y = 0
    heading = 0  # 0 = N, 1 = E, 2 = S, 3 = W
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for movement in dirs:
        if movement[0] == 'R':
            heading = (heading + 1) % 4
        elif movement[0] == 'L':
            heading = (heading - 1) % 4
        else:
            print "Malformed Move: Didn't start with L/R"

        length = int(movement[1:])

        x = x + deltas[heading][0] * length
        y = y + deltas[heading][1] * length

    print "x: {0}; y: {1}".format(x, y)
    print "distance: {0}".format(abs(x) + abs(y))


if __name__ == "__main__":
    main(sys.argv[1:])