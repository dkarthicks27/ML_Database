def berland(n, univ, stud_skill):
    univ_type = dict()
    for i in range(0, len(univ)):
        if univ[i] in univ_type:
            univ_type[univ[i]].append(i)
        else:
            univ_type[univ[i]] = [i]


    tot_array = []
    for i in range(1, n+1):
        tot = 0
        for university in univ_type:
            if len(univ_type[university]) >= i:
                
            pass

    print(univ_type)
    print('\n\n')
    pass



if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        univ = list(map(int, input().split()))
        stud_skill = list(map(int, input().split()))
        berland(n, univ, stud_skill)
