def check_no(number):
    dividend = int('1' * len(str(number)))
    if dividend > number:
        dividend = int('1' * (len(str(number)) - 1))
    while number > 11:
        if number % dividend == 0:
            return 'YES'
        elif number % dividend < 11:
            return 'NO'
        else:
            print(f'number: {number}, dividend: {dividend}')
            number = number % dividend
            dividend = int('1' * len(str(number)))
            if dividend > number:
                dividend = int('1' * (len(str(number)) - 1))
            print(f'number: {number}, dividend: {dividend}')

        print('\n')

    return 'NO'


if __name__ == '__main__':
    # so given a number our job is to find if the number could be a possible sum of a combination of 11, 111, 1111, ..

    # for eg: 33 could be 11 + 11 + 11
    # and also 144 could be 111 + 11 + 11 + 11

    # so the first thing that we might notice is that the number of digits in given num is the
    # same as the maximum number of 1's

    # so for example 33 cannot be any more than 11, it cant have 111. similarly 99 cannot have 111 and above
    # print(check_no(2047))
    t = 69
    for _ in range(t):
        num = int(input())
        ans = check_no(num)
        print(ans)


