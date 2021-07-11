import string



if __name__ == '__main__':
    t = int(input())
    letters = [i for i in string.ascii_lowercase]
    for _ in range(t):
        x = input()
        p = set(letters[:len(x)])
        q = set(x)


        if p == q:
            res = [letters.index(i) for i in x]
            st = 0
            err = 0
            while True:
                start = res.index(st)
                if len(res) == 1:
                    break
                else:
                    nearest = st + 1
                    nea_st = res.index(nearest)
                    if start + 1 == nea_st or start - 1 == nea_st:
                        res.remove(st)
                        st += 1
                    else:
                        err = 1
                        break

            if err:
                print('NO')
            else:
                print('YES')

        else:
            print('NO')
