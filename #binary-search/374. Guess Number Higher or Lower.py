'''374. Guess Number Higher or Lower
Solved
Easy
Topics
Companies
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1
 

Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

Seen this question in a real interview before?
1/5
Yes
No
Accepted
752.9K
Submissions
1.4M
Acceptance Rate
54.7%
Topics
Binary Search
Interactive'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low, high = 1, n

        while low <= high:
            mid = low + (high-low) //2
            result = guess(mid)

            if result == 0:
                return mid # found
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1
        



'''
Binary search works well because:
	1.	The numbers are sorted implicitly (1 to  n ).
	2.	The range is halved in each step, ensuring a logarithmic time complexity,  O(\log n) .

    1.	When  n = 1 :
	•	The range [low, high] is [1, 1]. The first guess will return the correct number.
	2.	When the number is at the boundaries:
	•	If the number is 1 or  n , the algorithm will find it as low or high reaches the correct value during the binary search.
'''