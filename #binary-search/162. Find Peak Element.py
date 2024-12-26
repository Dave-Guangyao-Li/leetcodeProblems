'''162. Find Peak Element
Solved
Medium
Topics
Companies
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.7M
Submissions
3.6M
Acceptance Rate
46.2%
Topics
Array
Binary Search'''


from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            # get the middle index
            mid = low + (high-low) //2

            # compare mid with right neighbor
            if nums[mid] > nums[mid+1]:
                # If mid is greater than its right neighbor,
                # move the high pointer to mid (peak lies to the left or at mid)
                high = mid
            else:
                # If mid is less than its right neighbor,
                # move the low pointer to mid + 1 (peak lies to the right)
                low = mid + 1

        # When low == high, we have found a peak
        return low



'''
	1.	Key Observations:
	•	A peak element is greater than its neighbors.
	•	If nums[mid] > nums[mid + 1], it implies there’s a peak on the left side or at mid.
	•	Otherwise, there’s a peak on the right side.
	2.	Binary Search:
	•	Start with two pointers, low at the beginning of the array and high at the end.
	•	Compute the middle index, mid.
	•	Compare nums[mid] with nums[mid + 1]:
	•	If nums[mid] > nums[mid + 1], move the high pointer to mid.
	•	Otherwise, move the low pointer to mid + 1.
	•	Stop when low == high; this index represents a peak.


    Time Complexity:
	•	The binary search reduces the search space by half at each step.
	•	For an array of size  n , the time complexity is  O(\log n) .

Space Complexity:
	•	The algorithm uses a constant amount of extra space:  O(1) .
'''