if __name__ == '__main__':
    n = int(input())
    li = list(map(int, input().split()))


    li = [x / 100 for x in li]
    print(sum(li)/n * 100)