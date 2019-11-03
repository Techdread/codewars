# Given an array/list [] of integers , Find the product of the k maximal numbers.
from functools import reduce
import operator

def max_product(lst, n_largest_elements):
    lst_largw = [x for x in sorted(lst)[::-1][:n_largest_elements]]
    return reduce(operator.mul, lst_largw, 1)

# Test.it("Basic Tests")
print(max_product([0]*10, 5))
print(max_product([4,3,5], 2))
print(max_product([10,8,7,9], 3)) # , 720)
print(max_product([8,6,4,6], 3)) #, 288)

# I like the reverse = true. sorted(lst, reverse=True) 
# much shorter consicse functional version
def max_product (lst, n):
    from functools import reduce
    from operator import mul
    return reduce(mul, sorted(lst, reverse=True)[:n])