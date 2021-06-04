if __name__ == '__main__':
    _ = input()
    array = list(map(int, input().split()))


    new_array = [0 for i in range(len(array))]
    for i in range(len(array)):
        new_array[array[i] - 1] = i+1

    print(' '.join([str(i) for i in new_array]))