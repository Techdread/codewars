# https: // www.codewars.com/kata/5772da22b89313a4d50012f7/train/python

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

print(greet('Daniel', 'Daniel'))
print(greet('Greg', 'Daniel'))

def greet(name, owner):
    return "Hello boss" if name == owner else "Hello guest"

def greet(name, owner):
    return "Hello {}".format("boss" if name == owner else "guest")