'''
https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
1431. Kids With the Greatest Number of Candies
Solved
Easy
Topics
Companies
Hint
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
 

Constraints:

n == candies.length
2 <= n <= 100
1 <= candies[i] <= 100
1 <= extraCandies <= 50

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.1M
Submissions
1.3M
Acceptance Rate
87.8%
Topics
Array'''


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Step 1: Find the current maximum candies among all kids
        max_candies = max(candies)
        # Step 2: Initialize the result array
        res = []
        # Step 3: Check each kid's condition
        for c in candies:
            # Calculate the total candies if this kid gets all extraCandies
            if c + extraCandies >= max_candies:
                # If total candies are greater than or equal to the max_candies, append True
                res.append(True)
            else:
                res.append(False)
        # Step 4: Return the result array
        return res


'''
	1.	Find the Maximum Candies:
	•	First, identify the current maximum candies any kid has in the candies array.
	2.	Simulate Each Kid’s Total:
	•	For each kid, calculate their total candies after adding the extraCandies.
	•	If the total is greater than or equal to the current maximum candies, mark the result as True. Otherwise, mark it as False.

This approach ensures we efficiently check each kid’s condition.
'''
