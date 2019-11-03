# took me less than five minutes to write.
def monkey_count(n):
    return list(range(1, n+1))

print(monkey_count(5))

# a more optimal solution leave out the list
def monkey_count_opt(n):
    return range(1, n+1)