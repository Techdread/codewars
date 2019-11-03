# Given an array/list [] of integers , Construct a product array Of same size Such That prod[i] is equal to The Product of all the elements of Arr[] except Arr[i].

def product_array(numbers):

    result = 1
    prod_list = list()
    # produce the product of the whole list
    for x in numbers: 
         result = result * x

    # divide the product by the current element in list and appen to new list.
    # also make sure an integer is returned
    for x in numbers:  
        prod_list.append(result // x)

    return prod_list

print(product_array([12,20]))
print(product_array([3,27,4,2]))
print(product_array([13,10,5,2,9]))
print(product_array([16,17,4,3,5,2]))


from operator import mul
from functools import reduce

def product_array_best(numbers):
    tot = reduce(mul,numbers)
    return [tot//n for n in numbers]