# Given an array of intgers , Find the minimum sum which is obtained from summing each Two integers product.

# Explanation: The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22


# I did well, would have liked to do a one liner
def min_sum(arr):
    arr=sorted(arr)
    return sum( a * b for a, b in zip(reversed(arr[:int(len(arr)/2)]), arr[int(len(arr)/2):])) 

print(min_sum([5,4,2,3]))
print(min_sum([12,6,10,26,3,24]))
print(min_sum([9,2,8,7,5,4,0,6]))


def min_sum_oneliner(arr):
    return sum(x * y for x, y in zip(sorted(arr)[::2], sorted(arr)[-1::-2]))

def min_sum_best(arr):
    arr = sorted(arr)
    return sum(arr[i]*arr[-i-1] for i in range(len(arr)//2))