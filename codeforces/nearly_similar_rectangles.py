from math import factorial


def nearlySimilarRectangles(sides):
    ref_dict = dict()
    for pair in sides:
        if pair[0] / pair[1] not in ref_dict:
            ref_dict[pair[0] / pair[1]] = 1
        else:
            ref_dict[pair[0] / pair[1]] += 1


    count = 0
    for key in ref_dict:
        if ref_dict[key] > 1:
            val = ref_dict[key]
            n_fact = factorial(val)
            r_fact = 2
            n_minus_r = factorial(val - 2)
            count += n_fact // r_fact // n_minus_r

    return count



sds = [[4, 8], [5, 10], [15, 30], [25, 50]]

nearlySimilarRectangles(sds)