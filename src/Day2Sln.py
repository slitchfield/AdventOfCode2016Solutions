

import sys

def main(argv):

    filename = argv[0]

    with open(filename, 'r') as fileptr:
        input_text = [line.rstrip() for line in fileptr.readlines()]

    print input_text

    digits_out = []

    num_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    x_idx = 1
    y_idx = 1

    deltas = {'R': (1, 0), 'L': (-1, 0), 'U': (0, -1), 'D': (0, 1)}

    for digit_line in input_text:

        for move in digit_line:

            x_idx = x_idx + deltas[move][0]
            y_idx = y_idx + deltas[move][1]

            if x_idx < 0:
                x_idx = 0
            elif x_idx > 2:
                x_idx = 2

            if y_idx < 0:
                y_idx = 0
            elif y_idx > 2:
                y_idx = 2

        digits_out.append(num_pad[y_idx][x_idx])

    print digits_out

if __name__ == "__main__":
    main(sys.argv[1:])