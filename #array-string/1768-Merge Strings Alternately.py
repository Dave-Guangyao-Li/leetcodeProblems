'''
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

1768. Merge Strings Alternately
Solved
Easy
Topics
Companies
Hint
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.2M
Submissions
1.5M
Acceptance Rate
81.2%
Topics
Two Pointers
String
'''


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Initialize pointers for both strings
        i, j = 0, 0
        # Initialize an empty list to store the merged characters
        merged = []

        # Step 1: Merge characters alternately while both pointers are in bounds
        while i < len(word1) and j < len(word2):
            merged.append(word1[i])
            i += 1
            merged.append(word2[j])
            j += 1

        # Step 2: Append remaining characters from word1, if any
        while i < len(word1):
            merged.append(word1[i])
            i += 1

        # Step 3: Append remaining characters from word2, if any
        while j < len(word2):
            merged.append(word2[j])
            j += 1

        # Step 4: Join the merged characters into a single string and return
        return "".join(merged)


'''
This problem can be solved using a two-pointer approach:
	1.	Use two pointers, i and j, to traverse word1 and word2 respectively.
	2.	Merge the characters alternately:
	•	Add a character from word1 if i is within bounds.
	•	Add a character from word2 if j is within bounds.
	3.	Append the remaining characters from the longer string when one string is exhausted.


    1.	Iteration:
	•	We iterate through both strings simultaneously, processing each character exactly once.
	•	Time complexity:  O(n + m) , where  n  is the length of word1 and  m  is the length of word2.
	2.	Space Complexity:
	•	The merged list stores  n + m  characters.
	•	Space complexity:  O(n + m) .
'''
