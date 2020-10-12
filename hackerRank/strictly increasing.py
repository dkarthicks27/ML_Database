def check_duplicate(arr):
    boolean = False
    seen = set()
    lastNonDuplicateIndex = None
    for i in range(len(arr)):
        if arr[i] not in seen:
            seen.add(arr[i])
            lastNonDuplicateIndex = i
        else:
            boolean = True
            break

    return boolean, lastNonDuplicateIndex



def increasing(arr):
    # player1 = 1
    # player2 = 2

    #   check if there is an duplicate in the array, if the answer is no then current player wins as he can easily sort it,
    #   if the answer is yes then i have to remove elements that are unique and if there are no unique elements then I have to remove
    #   one of the duplicate elements, as they

    player = 1

    if not check_duplicate(arr)[0]:
        return 'First'


    dup_exist, index = check_duplicate(arr)
    while dup_exist:
        if player % 2 == 1:
            print('first player:\n')
        else:
            print('second player:\n')
        print('initial array: ', arr)
        del arr[index]
        print('final arr: ', arr)
        print('\n')

        dup_exist, index = check_duplicate(arr)
        player += 1

        # if player % 2 == 1:
        #     print('first player:\n')
        # else:
        #     print('second player:\n')
        # print('initial array: ', arr)
        # remove = None
        # for i in range(len(arr)):
        #     if arr[i] not in duplicates:
        #         remove = i
        #         break
        #
        # if remove is not None:
        #     del arr[remove]
        # else:
        #     #   all the elements are duplicates so it is okay to delete any element
        #     del arr[0]
        # print('final arr: ', arr)
        # print('\n')
        # dup_exist, duplicates = check_duplicate(arr)
        # player += 1

    if player % 2 == 0:
        return 'Second'
    else:
        return 'First'


array = list(map(int, '1 2 2 3'.split()))
print(array)
print('\n\n')
print(increasing(array))
