import re


def removal(x):
    pattern = r'1{1,}'
    search = re.findall(pattern, x)
    search.sort(reverse=True)
    alice = 0
    for i in range(len(search)):
        if i % 2 == 0:
            alice += len(search[i])



    return alice



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        string = input()
        print(removal(string))