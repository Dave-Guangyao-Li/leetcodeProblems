'''
https://leetcode.com/problems/can-place-flowers/?envType=study-plan-v2&envId=leetcode-75
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

Seen this question in a real interview before?
1/5
Yes
No
Accepted
980.8K
Submissions
3.4M
Acceptance Rate
28.8%
Topics
Array
Greedy'''


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        # Special case: if no flowers need to be planted, return True
        if n == 0:
            return True

        # Step 1: Traverse the flowerbed
        for i in range(len(flowerbed)):
            # Step 2: Check if a flower can be planted at position `i`
            if flowerbed[i] == 0:  # The current plot is empty
                # Check the previous and next plots
                # Previous plot is empty or out of bounds
                prev_empty = (i == 0 or flowerbed[i - 1] == 0)
                # Next plot is empty or out of bounds
                next_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)

                if prev_empty and next_empty:
                    # Plant a flower at position `i`
                    flowerbed[i] = 1
                    n -= 1  # Decrement the number of flowers needed

                    # If all flowers are planted, return True
                    if n == 0:
                        return True

        # Step 3: If not enough flowers are planted, return False
        return n == 0


'''
	1.	Key Insight:
        •	A flower can be planted in a plot if:
        •	The plot is empty (flowerbed[i] == 0).
        •	The previous plot (flowerbed[i-1]) and the next plot (flowerbed[i+1]) are either empty or out of bounds.
	2.	Iterative Approach:
        •	Traverse the flowerbed array.
        •	Whenever a plot satisfies the conditions for planting a flower, plant it and decrement n.
        •	If n becomes 0, return True.
        •	If the loop completes and n > 0, return False.
	3.	Edge Cases:
        •	Very small flowerbed sizes ([0], [1], [0,0]).
        •	n = 0, which always returns True.

    1.	Traversal:
	•	We traverse the flowerbed array once.
	•	Time complexity:  O(f) , where  f  is the length of the flowerbed.
	2.	Space Complexity:
	•	We use no extra space besides variables.
	•	Space complexity:  O(1) .

'''
