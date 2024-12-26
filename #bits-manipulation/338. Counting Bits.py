'''
338. Counting Bits
Solved
Easy
Topics
Companies
Hint
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105
 

Follow up:

It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.3M
Submissions
1.6M
Acceptance Rate
79.1%
Topics
Dynamic Programming
Bit Manipulation'''

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)
        for i in range(n+1):
            # binary representation count 1s
            # For each ( i ):
            #     If ( i ) is even, set ans[i] = ans[i / 2].
            #     If ( i ) is odd, set ans[i] = ans[i - 1] + 1.
            result[i] = result[i>>1] + (i&1) # only add 1 when i is odd
        return result

'''
use a pattern:

If ( i ) is even, the number of 1s in ( i ) is the same as the number of 1s in ( i/2 ) (right-shifting an even number halves it without adding a new 1).
If ( i ) is odd, the number of 1s in ( i ) is the number of 1s in ( i - 1 ) plus one additional 1 (as adding 1 to an even number makes it odd).
'''