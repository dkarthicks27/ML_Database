if __name__ == '__main__':
    _ = input()

    charges = 0
    li = list(map(int, input().split()))
    max_charge = max(li)
    for i in li:
        charges += max_charge - i

    print(charges)