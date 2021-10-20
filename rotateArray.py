#Source: LeetCode
#Given an array, rotate the array to the right by k steps, where k is non-negative.


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(arr, l , r):
            for i in range((r-l)//2):
                arr[l+i], arr[r-1-i] = arr[r-1-i], arr[l+i]

        k = k % len(nums)

        rev(nums,len(nums)-k, len(nums))
        rev(nums, 0, len(nums)-k)
        rev(nums, 0 ,len(nums))

#notes: time complexity of O(n), space complexity of O(1)
