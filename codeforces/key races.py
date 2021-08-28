if __name__ == '__main__':
    s, v1, v2, t1, t2 = list(map(int, input().split()))
    first = s * v1 + 2 * t1
    second = s * v2 + 2 * t2

    if first > second:
        print('Second')
    elif first < second:
        print('First')
    else:
        print('Friendship')