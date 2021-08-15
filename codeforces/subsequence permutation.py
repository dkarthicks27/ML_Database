if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        string = input()
        arranged_string = sorted(string)
        diff = 0
        for i in range(n):
            if string[i] != arranged_string[i]:
                diff += 1

        print(diff)