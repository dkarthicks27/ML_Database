if __name__ == '__main__':
    n = int(input())
    commands = input()
    l_com = commands.count('L')
    r_com = commands.count('R')
    print(l_com + r_com + 1)
