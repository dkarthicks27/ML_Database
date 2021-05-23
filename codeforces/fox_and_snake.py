# if __name__ == '__main__':
#     n, m = list(map(int, input().split()))
#     snake_cell = '#'
#     empty_cell = '.'
#
#     for i in range(1, n+1):
#         if i % 2 == 1:
#             print(snake_cell * m)
#         else:
#             k = (i - 2)/4 + 1
#             if k.is_integer():
#                 print(empty_cell * (m - 1), snake_cell, sep='')
#             else:
#                 print(snake_cell, empty_cell * (m - 1), sep='')


circle_areas = [3.54773, 5.57778, 4.00014, 59.24241, 34.01344, 32.01013]

result = list(map(round, circle_areas, range(1,3)))
print(result)