def countdown(no, length):
    if int(no[-1]) == 0:
        total = 0
        for i in no:
            if int(i) != 0:
                total += int(i) + 1
        return total
    else:
        total = 0
        for i in range(length - 1):
            if int(no[i]) != 0:
                total += int(no[i]) + 1
        return total + int(no[length - 1])



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        number = input()
        count_down = countdown(number, n)
        print(count_down)
