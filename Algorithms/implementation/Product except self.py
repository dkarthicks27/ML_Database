inp = [1, 2, 3, 4]

# output [24, 12, 8, 6]


# so there are two ways to do this
# 1) naive way: in this I would actually iterate through each element and find product other than that element
# This solution will work but it is O(n^2) solution so we need better one


#
# method 1
# product = []
#
# for i in range(len(inp)):
#     prod = 1
#     for j in range(len(inp)):
#         if i != j:
#             prod *= inp[j]
#     product.append(prod)
#
# print(product)

# method 2
# finding the product of all elements
# and divinding by each element

prod = 1
for i in inp:
    prod *= i

product = []
for i in inp:
    product.append(prod // i)

print(product)