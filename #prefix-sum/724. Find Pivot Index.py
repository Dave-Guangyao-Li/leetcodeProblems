'''
724. Find Pivot Index
Solved
Easy
Topics
Companies
Hint
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0
 

Constraints:

1 <= nums.length <= 104
-1000 <= nums[i] <= 1000
 

Note: This question is the same as 1991: https://leetcode.com/problems/find-the-middle-index-in-array/


Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.3M
Submissions
2.1M
Acceptance Rate
59.2%
Topics
Array
Prefix Sum
'''

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums) # Calculate the total sum of all numbers
        left_sum = 0 # Cumulative sum of numbers to the left of index i
        
        for i in range(len(nums)):
            if left_sum == total_sum - nums[i] - left_sum: 
                return i
            left_sum += nums[i]
        return -1  # If no pivot index found, return -1

'''
you can calculate the cumulative sums once and access them directly during the loop.
Early termination: Once you find a pivot index, there is no need to continue checking the remaining indices. You can terminate the loop and return the pivot index immediately.
we calculate the total sum of all numbers in the nums list only once. Then, during the loop, we compare the current left_sum with the remaining sum on the right side (total_sum - left_sum - nums[i]). If they are equal, we have found a pivot index and return it immediately. Otherwise, we update left_sum and continue iterating.
These optimizations reduce the time complexity from O(n^2) to O(n), making the code more efficient.
'''