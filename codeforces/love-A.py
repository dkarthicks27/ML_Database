if __name__ == '__main__':
    inp = input()
    no_of_a = inp.count('a')
    if len(inp) <= (no_of_a * 2) - 1:
        print(len(inp))
    else:
        print((no_of_a * 2) - 1)