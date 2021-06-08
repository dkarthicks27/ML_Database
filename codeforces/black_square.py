if __name__ == '__main__':
    calorie_each_pos = input().split()
    ref = {str(i+1): int(calorie_each_pos[i]) for i in range(len(calorie_each_pos))}
    s = input()

    count = 0
    for i in s:
        count += ref[i]

    print(count)