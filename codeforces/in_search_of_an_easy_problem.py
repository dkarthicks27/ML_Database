if __name__ == '__main__':
    _ = input()
    li = list(map(int, input().split()))

    if any(li):
        print('hard')
    else:
        print('easy')