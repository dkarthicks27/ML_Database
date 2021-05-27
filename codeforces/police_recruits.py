if __name__ == '__main__':
    untreated_crime = 0
    num_of_officers = 0
    _ = input()
    crime_order = list(map(int, input().split()))
    # print(crime_order)
    for crime in crime_order:
        if crime == -1:
            if num_of_officers + crime >= 0:
                num_of_officers -= 1
            else:
                untreated_crime += 1

            # a crime has occurred
            pass
        elif crime > 0:
            num_of_officers += crime

    print(untreated_crime)