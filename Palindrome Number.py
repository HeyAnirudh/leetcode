class Solution(object):
    def isPalindrome(self, x):
        y = str(x)

        y = y[::-1]
        if x < 0:
            y = -1 * y

        if y == str(x):
            return True
        else:
            return False
