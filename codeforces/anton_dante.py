if __name__ == '__main__':
    _ = input()
    string = input()

    anton = string.count('A')
    danik = string.count('D')

    if anton > danik:
        print('Anton')
    elif danik > anton:
        print('Danik')
    else:
        print('Friendship')