def stones_on_table(string):
    remove = 0
    reference = string[0]
    for i in string[1:]:
        if i == reference:
            remove += 1
            reference = i
            continue

        reference = i

    return remove


if __name__ == '__main__':
    n = int(input())
    inp_str = input()
    ans = stones_on_table(inp_str)
    print(ans)