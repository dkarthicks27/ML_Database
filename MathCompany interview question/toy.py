# so we are given n number of toys and their prices, we have to find the maximum number of consecutive toys we can
# buy in our budget,
# The condition given is that we can actually choose any one type of type as free and pay for the rest


# so we have to find the optimal solution, below is an sample test case

# INPUT
# 6 10                                                          -----------> N ( number of toys ) , M (given money)
# aabcda                                                        -----------> n number of toys given as string
# 5 4 4 5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1           -----------> price of all the 26 toys in the eng

# OUTPUT
# 4




if __name__ == '__main__':
    string = 'aabcda'
    array = []
    dictionary = {'a': -5, 'b': 4, 'c': 4, 'd': 5, 'e': 1, 'f': 1, 'g': 1, 'h': 1, 'i': 1, 'j': 1, 'k': 1, 'l': 1, 'm': 1, 'n': 1, 'o': 1, 'p': 1, 'q': 1, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 1, 'w': 1, 'x': 1, 'y': 1, 'z': 1}
    for i in string:
        array.append(dictionary[i])
    print(array)
    m = 10
    local_max = global_max = array[0]
    for i in range(1, len(array)):
        print(array[i], local_max + array[i], sep=' or ', end='       ')
        local_max = max(array[i], local_max + array[i])

        if local_max > global_max:
            global_max = local_max
        print(local_max, global_max)

    print(global_max)