def solve(t1, t2):
    count = 0
    # code here
    home_t1 = t1[0]
    away_t1 = t1[1]
    home_t2 = t2[0]
    away_t2 = t2[1]

    # this is the match where host is t1 and away is t2
    # in that case host will wear home jersey and away will wear away jersey
    if home_t1 == away_t2:
        count += 1
    if home_t2 == away_t1:
        count += 1
    # now the opposite scenario

    return count


if __name__ == '__main__':
    n = int(input())

    teams = []
    for _ in range(n):
        teams.append(tuple(map(int, input().split())))

    jersey_changes = 0

    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            jersey_changes += solve(teams[i], teams[j])


    print(jersey_changes)