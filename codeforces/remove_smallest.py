def if_possible(array):
    for i in range(1, len(array)):
        if array[i] - array[i - 1] > 1:
            return 'NO'
    return 'YES'




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ans = if_possible(sorted(list(map(int, input().split()))))
        print(ans)
