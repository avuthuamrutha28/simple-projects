#sum of squares of even numbers
from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = filter(lambda x: x % 2 == 0, lst)
squares = map(lambda x: x * x, evens)
result = reduce(lambda x, y: x + y, squares)
print(result)
