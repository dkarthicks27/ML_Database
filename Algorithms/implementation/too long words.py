n = int(input())


i = 0
while i < n:
    word = list(input())
    if len(word) > 10:
        print(f'{word[0]}{len(word[1:-1])}{word[-1]}')
    else:
        print(''.join(word))
    i += 1
