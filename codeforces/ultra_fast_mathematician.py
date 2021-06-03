if __name__ == '__main__':
    a = input()
    b = input()

    print(bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a)))