if __name__ == '__main__':
    inp = int(input())
    count = 0
    for _ in range(inp):
        if '++' in input():
            count += 1
        else:
            count -= 1

    print(count)