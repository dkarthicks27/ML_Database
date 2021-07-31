if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        b = [int(i) for i in input()]

        a = [1]
        for i in range(1, n):
            if b[i - 1] + a[i - 1] != b[i] + 1:
                a.append(1)
            else:
                a.append(0)

        print(''.join(map(str, a)))

        # if b[0] == '1':
        #     res_arr = '2'
        # else:
        #     res_arr = '1'
        #
        # a = '1'
        # for i in range(n - 1):
        #     if int(b[i + 1]) + 1 != int(res_arr[i]):
        #         res_arr += str(int(b[i+1]) + 1)
        #         a += '1'
        #     else:
        #         res_arr += b[i+1]
        #         a += '0'
        #
        # print(a)
