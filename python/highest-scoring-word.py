# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position i the alphabet: a = 1, b = 2, c = 3 etc.
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.
# https://www.codewars.com/kata/highest-scoring-word/train/python
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/solutions/python

# refactored
def high(x):
    words = x.split()
    words_score = [sum(ord(x)-96 for x in word) for word in words]
    return words[max(range(len(words_score)), key=words_score.__getitem__)]

# This worked now try to refactor
def first_high(x):
    words = x.split()
    index = 0
    score = 0
    for word in words:
        x = sum(ord(x)-96 for x in word)
        if x > score:
            score = x
            greatest = index
        index=index+1
    return words[greatest]

print(high('man i need a taxi up to ubud')) # 'taxi')
print(high('what time are we climbing up the volcano')) # 'volcano')
print(high('take me to semynak')) #'semynak')

def best_high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))
