if __name__ == '__main__':
    n = int(input())
    string = input()
    even = 0
    for i in range(n):
        if int(string[i]) % 2 == 0:
            even += i + 1

    print(even)