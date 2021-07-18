def canBeTypedWords(text, broken):
    br = set(broken)
    count = 0
    for i in text.split(' '):
        if not set(i).intersection(br):
            count += 1

    return count



if __name__ == '__main__':
    text = "hello world"
    brokenLetters = "ad"
    print(canBeTypedWords(text, brokenLetters))