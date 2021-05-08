def no_divisors(number):
    if number == 1:
        return 1
    else:
        count = 0
        for i in range(1, number+1):
            if number % i == 0:
                count += 1
        return count


if __name__ == '__main__':
    inp_array = list(map(int, '1 2 3 4 5 6 7 8 9'.split(' ')))
    temp_dict = dict()
    for element in inp_array:
        divisors = no_divisors(element)
        if not temp_dict.get(divisors):
            temp_dict[divisors] = [element]
        else:
            temp_dict[divisors].append(element)

    final_array = []
    # print(temp_dict)
    for val in sorted(temp_dict.keys()):
        final_array.extend(sorted(temp_dict[val], reverse=True))

    print(final_array)
