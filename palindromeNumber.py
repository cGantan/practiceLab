#source: LeetCode
#task:
#Given an integer x, return true if x is palindrome integer without converting to a string. An integer is a palindrome when it reads the same backward as forward

class Solution(object):
    def isPalindrome(self, x):
        #approach: build up value from the back and check if it is equal to x
        temp = x//10
        backwards = x %10
        while temp > 0:
            backwards = backwards*10 + (temp % 10)
            temp = temp//10
        if backwards == x:
            return True
        return False
