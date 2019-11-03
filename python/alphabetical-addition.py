# Your task is to add up letters to one letter.
# The function will be given a variable amount of arguments, each one being a letter to add.
# https://www.codewars.com/kata/5d50e3914861a500121e1958
# https://www.codewars.com/kata/5d50e3914861a500121e1958/solutions/python

def add_letters(*letters):
    char_num = 0
    for character in letters:
        char_num = char_num + ord(character) - 96
    
    if (char_num == 0 or char_num % 26 == 0):
        return "z"
    else:
        return chr(char_num % 26 + 96)        

print(add_letters('z'))

# Best clever
def add_letters_clever(*letters):
    return chr( (sum(ord(c)-96 for c in letters)-1)%26 + 97)

# Nice 
num = 'abcdefghijklmnopqrstuvwxyz'
def add_letters_nice(*letters):
    x = 0
    x = sum(num.index(i)+1 for i in letters)
    while x-1 > 25:
        x -= 26
        
    return num[x-1]