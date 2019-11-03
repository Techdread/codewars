# Sum of all the multiples of 3 or 5
# liked this one quite easy to do. some of the solutions i found are much better

def find(n):
    unique_multiples = set()
    n+=1
    [unique_multiples.add(var) or var for var in range(0, n, 3) if var not in unique_multiples]
    [unique_multiples.add(var) or var for var in range(0, n, 5) if var not in unique_multiples]
    return sum(unique_multiples)
print(find(5))
print(find(10))

# very readable, scored best in best practise. 
def find_very_readable(n):
    sum = 0
    for i in range(1,n+1):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum

# good one liner dont understand the nots
def find_one_liner(n):
    return sum([x for x in range(1,n+1) if not x%3 or not x%5])


def find(n):
    return sum(range(0, n+1, 3)) + sum(range(0, n+1, 5)) - sum(range(0, n+1, 15))

def find(n):
    return sum( set(range(0, n+1, 3)) | set(range(0, n+1, 5)) )

def find(n):
    return sum(i for  i in range(n+1) if i % 3 == 0 or i % 5 == 0)