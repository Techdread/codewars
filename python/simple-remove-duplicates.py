# Simple remove duplicates
# liked this one but seen better answers with better in placed reverse
def solve(arr): 
    unique_set = set()
    unique_list = list()
    for i in reversed(arr):
        if i not in unique_set:
            unique_set.add(i)
            unique_list.append(i)
    unique_list.reverse()
    return unique_list

print(solve([3,4,4,3,6,3]))
print(solve([1,2,1,2,1,2,3]))
print(solve([1,2,3,4]))
print(solve([1,1,4,5,1,2,1]))

# like the inplace reverse same also as mine
def solve_better(arr): 
    re = []
    for i in arr[::-1]:
        if i not in re:
            re.append(i)
    return re[::-1]

# this clever one liner
def solve_oneliner(arr): 
    return list(dict.fromkeys(arr[::-1]))[::-1]

# Another nice one
def solve_nice(arr): 
    seen = set()
    return [seen.add(a) or a for a in reversed(arr) if a not in seen][::-1]
