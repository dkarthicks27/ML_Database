import numpy as np

if __name__ == '__main__':
    inp = [[1, 0, 0], [0, 0, 1], [1, 0, 0]]

    # creating a matrix
    array = np.array(inp)
    count = 0

    for row in range(len(array)):
        # checking if there is only one 1 in a given row
        if sum(array[row]) == 1:
            col_idx = list(array[row]).index(1)
            # checking if it is the only 1 in the given column
            if sum(array[:, col_idx]) == 1:
                count += 1

    print(count)
