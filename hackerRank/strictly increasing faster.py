def strictlyIncreasing(arr):
    seen = set()
    dups = set()
    count = 0
    for i in arr:
        if i not in seen:
            seen.add(i)
        else:
            dups.add(i)
            count += 1

    return seen, count, dups


if __name__ == '__main__':
    array = [1, 2, 2, 3]
    allElem, noOfDups, dups = strictlyIncreasing(array)
    print('No. of Unique elements = ', len(allElem) - len(dups))
    print('No. of duplicates =', noOfDups)
    print('total actuall duplicates = ', len(dups))
    if noOfDups == 0:
        print('First')
    else:
        winner = len(allElem) - len(dups) + noOfDups + len(dups)
        print(winner)
        print('\n')
        if winner % 2 == 0:
            print('Second')
        else:
            print('First')
