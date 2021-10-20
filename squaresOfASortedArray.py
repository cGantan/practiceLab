#Source: LeetCode
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        point = 0
        res = []

        i = 0
        j = len(nums) - 1
        while (i < j):
            i_pow = pow(nums[i], 2)
            j_pow = pow(nums[j], 2)
            if (i_pow < j_pow):
                res = [j_pow] + res
                j -= 1
            else:
                res = [i_pow] + res
                i += 1
        i_pow = pow(nums[i], 2)
        res = [i_pow] + res
        return res

#notes: O(n) space and time complexity
