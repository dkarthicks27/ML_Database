if __name__ == '__main__':
    string = input()
    if len(string) != 1:
        x = list(map(str, sorted(list(map(int, string.split('+'))))))
        print('+'.join(x))

    else:
        print(string)