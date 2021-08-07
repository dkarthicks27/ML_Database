if __name__ == '__main__':
    # l = 10 , r = 15
    # x = 10, 11, 12, 13, 14, 15
    # 12, 15

    l, r = list(map(int, input().split()))
    exit_condition = False
    for x in range(l, r+1):
        new_set = set(str(x))
        if len(new_set) == len([i for i in str(x)]):
            print(x)
            exit_condition = True
            break

    if not exit_condition:
        print(-1)