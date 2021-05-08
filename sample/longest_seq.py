if __name__ == '__main__':
    array = sorted([1, 3, 4, 5, 2, 9, 10, 11])
    prev_sum = array[0]
    longest_cons_seq = 0

    for i in array[1:]:
        if prev_sum + 1 == i:
            prev_sum = i
            longest_cons_seq += 1
        else:
            if longest_cons_seq > 0:
                break
            prev_sum = i

    print(longest_cons_seq + 1)
