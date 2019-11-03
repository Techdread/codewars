# My List Filtering code in python for code warriors. 

def filter_list(l):
    return [var for var in l if type(var) == int]

lst = filter_list([1,2,'a','b'])
print(type(lst))
print(*filter_list([1,2,'a','b']))
print(*filter_list([1,'a','b',0,15]))
print(*filter_list([1,2,'aasf','1','123',123]))