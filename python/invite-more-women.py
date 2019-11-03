# https://www.codewars.com/kata/58acfe4ae0201e1708000075/train/python

from Test import Test

def invite_more_women(arr):
    return False if sum(arr) <= 0 else True

# best solution
def invite_more_women_best(arr):
    return sum(arr) > 0

# Nice Solurion
def invite_more_women_nice(arr):
    return arr.count(1) > arr.count(-1)

testing = Test()

testing.describe("Basic Tests")
testing.assert_equals(invite_more_women([1, -1, 1]),True)
testing.assert_equals(invite_more_women([-1, -1, -1]),False)
testing.assert_equals(invite_more_women([1, -1]),False)
testing.assert_equals(invite_more_women([1, 1, 1]),True)
testing.assert_equals(invite_more_women([]),False)

testing.report()