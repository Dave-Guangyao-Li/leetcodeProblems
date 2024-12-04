'''345. Reverse Vowels of a String
Easy
Topics
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.1M
Submissions
1.9M
Acceptance Rate
55.5%
Topics
Two Pointers
String'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        # Step 1: Define a set of vowels for quick lookup
        vowels = set('aeiouAEIOU')
        # Convert the string to a list of characters (strings are immutable in Python)
        chars = list(s)
        # Initialize two pointers
        left, right = 0, len(chars) - 1

        # Step 2: Use two pointers to find and swap vowels
        while left < right:
            # Move left pointer until a vowel is found
            while left < right and chars[left] not in vowels:
                left += 1
            # Move right pointer until a vowel is found
            while left < right and chars[right] not in vowels:
                right -= 1
            # Swap the vowels at left and right
            chars[left], chars[right] = chars[right], chars[left]
            # Move both pointers inward
            left += 1
            right -= 1

        # Step 3: Convert the list back to a string and return
        return "".join(chars)


'''
This problem can be efficiently solved using the two-pointer technique:
	1.	Identify Vowels:
	•	The vowels are: {'a', 'e', 'i', 'o', 'u'} and their uppercase equivalents.
	•	Use a set to check if a character is a vowel in  O(1)  time.
	2.	Two Pointers:
	•	Place one pointer at the start (left) and another at the end (right) of the string.
	•	Swap vowels encountered at left and right.
	•	Move left and right inward until they meet.

	1.	Two Pointers:
	•	Each character is processed at most once as left and right move inward.
	•	Time complexity:  O(n) , where  n  is the length of the string.
	2.	Space Complexity:
	•	We use  O(1)  extra space for the two pointers and the vowel set.
	•	Converting the string to a list costs  O(n) , but that’s unavoidable in Python.

'''
