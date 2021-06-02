if __name__ == '__main__':
    n, m, p = list(map(int, input().split()))
    count_dict = dict()

    for _ in range(n):
        li = input()
        for i in range(len(li)):
            if count_dict.get(i):
                count_dict[i] += int(li[i])
            else:
                count_dict[i] = int(li[i])

    final_str = ''
    for key, val in count_dict.items():
        if val >= round(n/2):
            final_str += '1'
        else:
            final_str += '0'

    
    print(final_str)
