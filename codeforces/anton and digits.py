if __name__ == '__main__':
    arr = [2, 3, 5, 6]
    other_arr = list(map(int, input().split()))
    ref_dict = {arr[i]: other_arr[i] for i in range(4)}
    # print(ref_dict)
    total = 0
    p = min(ref_dict[5], ref_dict[6], ref_dict[2])
    if p > 0:
        total += p * 256
        # print(f'total : {total}, no of 256 is : {p}')

    if ref_dict[2] > p:
        q = ref_dict[2] - p
        k = min(q, ref_dict[3])
        if k > 0:
            total += k * 32
            # print(f'total : {total}, no of 32 is : {q}')

    print(total)
