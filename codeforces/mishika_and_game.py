if __name__ == '__main__':
    n = int(input())
    mike = 0
    chris = 0
    for _ in range(n):
        m, c = list(map(int, input().split()))
        if m > c:
            mike += 1
        elif m < c:
            chris += 1
        else:
            mike += 1
            chris += 1

    if mike > chris:
        print("Mishka")
    elif mike < chris:
        print("Chris")
    else:
        print("Friendship is magic!^^")