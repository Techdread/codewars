# Given an array/list [] of integers , Find the Nth smallest element in this array of integers
def nth_smallest(arr, pos):
    return sorted(arr)[pos - 1]

print(nth_smallest([3,1,2],2))
print(nth_smallest([-102,-16,-1,-2,-367,-9],5))

# I found the best solution