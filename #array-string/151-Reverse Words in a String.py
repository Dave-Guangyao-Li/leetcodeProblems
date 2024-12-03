'''
151. Reverse Words in a String
Solved
Medium
Topics
Companies
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.
 

Constraints:

1 <= s.length <= 104
s contains English letters (upper-case and lower-case), digits, and spaces ' '.
There is at least one word in s.
 

Follow-up: If the string data type is mutable in your language, can you solve it in-place with O(1) extra space?


Seen this question in a real interview before?
1/5
Yes
No
Accepted
2M
Submissions
4.1M
Acceptance Rate
48.0%
Topics
Two Pointers
String'''


class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Split the string into words
        # The split() method splits by spaces and removes extra spaces
        words = s.split()  # Example: "  hello   world  " -> ["hello", "world"]
        # Step 2: Reverse the list of words
        # Reversing the list puts the words in reverse order
        # Example: ["hello", "world"] -> ["world", "hello"]
        reversed_words = words[::-1]
        # Step 3: Join the words with a single space
        # Join combines the reversed words into a single string with spaces
        # Example: ["world", "hello"] -> "world hello"
        result = " ".join(reversed_words)

        return result


'''
	1.	Split the String into Words:
	•	Remove extra spaces, including leading, trailing, and between words.
	•	Use a split operation that handles spaces.
	2.	Reverse the List of Words:
	•	Reverse the order of the words using Python’s slicing.
	3.	Join the Words:
	•	Use the join method to concatenate the words with a single space.



    1.	Splitting the String:
	•	Splitting involves traversing the string once, so it takes  O(n) , where  n  is the length of the string.
	2.	Reversing the List:
	•	Reversing a list of words takes  O(k) , where  k  is the number of words.
	3.	Joining the Words:
	•	Joining the words back into a string takes  O(n) .

    Space Complexity:
	•	The space required for storing the list of words is  O(n) .

'''
