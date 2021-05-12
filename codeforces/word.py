if __name__ == '__main__':
    word = input()

    count_low = 0
    count_upp = 0

    for i in word:
        if i.isupper():
            count_upp += 1
        elif i.islower():
            count_low += 1

    word_ret = ''
    if count_upp > count_low:
        for i in word:
            if i.islower():
                word_ret += i.upper()
                continue
            word_ret += i

    else:
        for i in word:
            if i.isupper():
                word_ret += i.lower()
                continue
            word_ret += i

    print(word_ret)
