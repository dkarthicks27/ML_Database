def rgb(query):
    red, blue, green = query
    if not (r.get(red) and b.get(blue) and g.get(green)):
        return 'NO'
    r1 = r.get(red)
    b1 = b.get(blue)
    g1 = g.get(green)
    a = [r1, b1, g1]
    final = set().union(*a)
    if query in final:
        return 'YES'
    else:
        x, y, z = 0, 0, 0
        for i in r1:
            if i[1] <= query[1] and i[2] <= query[2]:
                x = 1
                break
        for i in b1:
            if i[0] <= query[0] and i[2] <= query[2]:
                y = 1
                break
        for i in g1:
            if i[1] <= query[1] and i[0] <= query[0]:
                z = 1
                break

        if x * y * z:
            return 'YES'

        return 'NO'



if __name__ == '__main__':
    n, q = input().split()
    r = {}
    b = {}
    g = {}

    for _ in range(int(n)):
        ri, bi, gi = list(map(int, input().split()))
        if not r.get(ri):
            r[ri] = {(ri, bi, gi)}
        else:
            r[ri].add((ri, bi, gi))


        if not b.get(bi):
            b[bi] = {(ri, bi, gi)}
        else:
            b[bi].add((ri, bi, gi))


        if not g.get(gi):
            g[gi] = {(ri, bi, gi)}
        else:
            g[gi].add((ri, bi, gi))

    i = 0
    while i < int(q):
        qr, br, gr = list(map(int, input().split()))
        print(rgb((qr, br, gr)))
        i += 1
