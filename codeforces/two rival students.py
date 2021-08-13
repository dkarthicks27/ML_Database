if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, x, a, b = list(map(int, input().split()))
        stud_line = list(range(1, n+1))
        # so the one closer to left will move towards left and that towards right will do that

        right_most = max(a, b)
        left_most = min(a, b)
        while x:
            if left_most != 1:
                left_most -= 1
                x -= 1
            elif right_most != n:
                right_most += 1
                x -= 1
            else:
                break

        print(right_most - left_most)