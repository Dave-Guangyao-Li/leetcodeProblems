'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75 
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
622.5K
Submissions
1.2M
Acceptance Rate
52.2%
Topics
Math
String
'''


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Step 1: Check if concatenating str1 + str2 equals str2 + str1
        # If not, there is no common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Step 2: Compute the GCD of the lengths of str1 and str2
        gcd_len = gcd(len(str1), len(str2))

        # Step 3: Return the prefix of length gcd_len from str1
        return str1[:gcd_len]


'''
Euclidean Algorithm to compute the GCD efficiently. Given two integers a and b, the GCD is calculated as gcd(a, b) = gcd(b, a % b) This process repeats until b = 0, at which point gcd(a, b) = a.


	1.	String Concatenation Check:
	•	Concatenating str1 + str2 and str2 + str1 takes  O(n + m) , where  n  and  m  are the lengths of str1 and str2.
	2.	GCD Calculation:
	•	The GCD of two integers is computed in  O(\log(\min(n, m)))  using the Euclidean algorithm.
	3.	Substring Extraction:
	•	Extracting a substring of length gcd_len takes  O(gcd_len) , which is at most  O(\min(n, m)) .
    O(n + m + \log(\min(n, m)))


    	1.	Check Concatenation:
	•	str1 + str2 = "ABCABCABC".
	•	str2 + str1 = "ABCABCABC".
	•	Since they are equal, we proceed.
	2.	Compute GCD of Lengths:
	•	len(str1) = 6, len(str2) = 3.
	•	 gcd(6, 3) = 3 .
	3.	Extract Prefix:
	•	The prefix of length 3 in str1 is "ABC".
	•	Validate: "ABCABC" is a multiple of "ABC", and "ABC" is also a multiple of "ABC".
	•	Result: "ABC".
'''
