if __name__ == '__main__':
    # so here we need to find total distinct characters

    inp = input()
    if len(inp) == 2:
        print(0)
    else:
        string = inp[1:-1]
        print(len(set(string.split(', '))))
