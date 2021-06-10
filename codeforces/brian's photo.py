if __name__ == '__main__':
    rows, col = list(map(int, input().split()))
    run = 0
    for row in range(rows):
        x = input()
        if 'C' in x or 'M' in x or 'Y' in x:
            run = 1
            print('#Color')
            break

    if not run:
        print('#Black&White')