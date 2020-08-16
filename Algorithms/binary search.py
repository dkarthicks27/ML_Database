def binary_search(array, item):
    minimum = 0
    maximum = len(array) - 1
    found = False
    iteration = 0
    while not found:
        iteration += 1
        avg = round((maximum + minimum)/2)
        if array[avg] == item:
            return avg, iteration
        elif array[avg] < item:
            minimum = avg + 1
        elif array[avg] > item:
            maximum = avg - 1



def linear_search(array, item):
    for i in range(len(array)):
        if array[i] == item:
            return i



if __name__ == '__main__':
    # so this program is very simple
    # we pass it a sorted array and a value to be found it will return us the index of that element
    # All the elements in the array are unique and no duplicate values are there
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    result, loops = binary_search(primes, 67)
    print(f'{loops} iteration were needed to find {primes[result]} whose index is {result}')
    result = linear_search(primes, 67)
    print(f'{result} iteration were required to find {primes[result]} whose index is {result}')
    pass
