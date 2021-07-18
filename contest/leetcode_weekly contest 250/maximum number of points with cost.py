def maxPoints(points):
    new_arr = [[0 for i in range(len(points[0]))] for j in range(len(points))]
    new_arr[0] = points[0]
    m = len(points)
    n = len(points[0])
    for i in range(1, m):
        for j in range(n):
            new_arr[i][j] = max([points[i][j] + new_arr[i - 1][y] - abs(y - j) for y in range(n)])

    print(max(new_arr[-1]))



if __name__ == '__main__':
    points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]
    maxPoints(points)
