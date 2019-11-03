# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.

def adjacent_element_product(array):
    max = array[0] * array[1]  
    for first, second in zip(array, array[1:]):
        if first * second > max:
            max = first * second
    return max

print(adjacent_element_product([5, 8]))
print(adjacent_element_product([1, 2, 3]))
print(adjacent_element_product([2, 2, 4]))

# best solution 
def adjacent_element_product_best(array):
    return max( a*b for a, b in zip(array, array[1:]) )