import numpy as np
import sys

def solved(x, y, a, b):

    A = np.array([[a, b], [b, a]])
    B = np.array([x, y])
    try:
        sol = list(np.linalg.solve(A, B))
        print(sum(sol), '\n')
    except:
        print(sys.exc_info(), '\n', f'Error is : X, Y, a, b: {(x, y, a, b)}\n\n')
        pass


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        x_, y_, a_, b_ = list(map(int, input().split()))
        solved(x_, y_, a_, b_)