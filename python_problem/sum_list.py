#sum of the list
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res_sum = reduce(lambda x, y: x + y, lst)
print(res_sum)
