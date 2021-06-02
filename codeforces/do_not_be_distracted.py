if __name__ == '__main__':
    t = int(input())


    for _ in range(t):
        n = input()
        pattern = input()
        index_dict = dict()

        sus = 'YES'
        for i in range(len(pattern)):
            if pattern[i] not in index_dict:
                index_dict[pattern[i]] = i

            else:
                curr_index = i
                if curr_index - index_dict[pattern[i]] > 1:
                    sus = 'NO'
                    break

                elif curr_index - index_dict[pattern[i]] == 1:
                    index_dict[pattern[i]] = curr_index

        print(sus)