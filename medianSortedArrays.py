#source:LeetCode
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        med_index = len(nums1)+len(nums2)
        two_mids = False
        if (med_index % 2 == 0):
            two_mids = True
        med_index = med_index//2

        i = -1
        one_i = 0
        two_i = 0
        curr_in_one = True
        prev_in_one = True

        while (i != med_index):
            prev_in_one = curr_in_one
            if (len(nums1) > one_i and len(nums2) > two_i):
                if (nums1[one_i] > nums2[two_i]):
                    curr_in_one = False
                    two_i += 1
                else:
                    curr_in_one = True
                    one_i += 1
            elif (len(nums1) <= one_i):
                curr_in_one = False
                two_i += 1
            else:
                curr_in_one = True
                one_i += 1
            i += 1
        if (not two_mids):
            if (curr_in_one):
                return nums1[one_i-1]
            else:
                return nums2[two_i-1]
        else:
            res = 0
            if (curr_in_one):
                res = nums1[one_i-1]
            else:
                res= nums2[two_i-1]
            if (prev_in_one and curr_in_one):
                res = res + nums1[one_i-2]
            elif (not prev_in_one and not curr_in_one):
                res = res + nums2[two_i-2]
            elif (not prev_in_one):
                res = res + nums2[two_i-1]
            else:
                res = res+ nums1[one_i-1]
            return float(res)/2
        return 0
