if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()
        arr = []
        for i in range(len(string)):
            if i % 2 == 0:
                if string[i] == 'a':
                    arr.append('b')
                else:
                    arr.append('a')

            else:
                if string[i] == 'z':
                    arr.append('y')
                else:
                    arr.append('z')

        print(''.join(arr))