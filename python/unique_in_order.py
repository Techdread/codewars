#Implement the function unique_in_order which takes as argument a sequence 
# and returns a list of items without any elements with the same value 
# next to each other and preserving the original order of elements.
# https://www.codewars.com/kata/54e6533c92449cc251001667/train/python

def unique_in_order(iterable):
    unique = []
    for n in iterable:
        if len(unique) == 0:
            unique.append(n)
        if n != unique[-1]:
            unique.append(n)
    return unique

unique_in_order([1,2,2,3,3]) 
unique_in_order('AAAABBBCCDAABBB')