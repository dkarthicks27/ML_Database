from string import ascii_lowercase


def prefix_sums(A):
    n = len(A)
    P = [0] * (n+1)
    for k in range(1, n+1):
        P[k] = P[k-1] + ref_dict[A[k-1]]

    return P


if __name__ == '__main__':
    n, q = list(map(int, input().split()))
    string = input()
    ref_dict = dict()
    for i in range(len(ascii_lowercase)):
        ref_dict[ascii_lowercase[i]] = i+1

    p = prefix_sums(string)
    for _ in range(q):
        i, j = list(map(int, input().split()))
        print(p[j] - p[i-1])
