if __name__ == '__main__':
    n = int(input())
    notes = 0
    money = [100, 20, 10, 5, 1]
    for curr in money:
        if n % curr != n:
            notes += n // curr
            n = n % curr

    print(notes)