if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    li = list(map(int, input().split()))

    new_li = [i for i in li if i + k <= 5]
    if new_li:
        print(len(new_li) // 3)
    else:
        print(0)
