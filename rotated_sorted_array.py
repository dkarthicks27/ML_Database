if __name__ == '__main__':
    # inp = [5, 6, 7, 8, 1, 2, 3]
    inp = [2, 3, 4, 5, 6, 1]
    start = 0
    end = len(inp) - 1
    print(inp[start], inp[end], inp[(start + end) // 2])
    while 1:
        mid = (start + end) // 2

        if inp[mid] > inp[start]:
            start = mid
        elif inp[end] > inp[mid]:
            end = mid

        if inp[end] == inp[mid] and inp[end] > inp[start]:
            print(inp[start])
            break

        central_ele = inp[mid]
        left = inp[mid - 1]
        right = inp[mid + 1]


        if left > central_ele and right > central_ele:
            print(central_ele)
            break

