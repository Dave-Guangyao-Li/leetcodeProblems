'''
# Oh no! We've lost all the spaces in our sentence. 
# Create a function to re-separate it back into words. 

string = "thedogbarks"
expected_output = ["the", "dog", "barks"]
 
vocabulary = ["dog", "the", "away", "barks"]

string = "thedogbarks"
vocabulary = ["dog", "the", "away", "barks”, "he"
'''

# not optimal segmentaion, has overlap


def separate_str(cur_str, vocabulary):
    result = []
    vocab_set = set(vocabulary)  # {"dog", "the", "away", "barks"}
    # print(vocab_set)
    for i in range(len(cur_str)):
        for j in range(i+1):
            if cur_str[j:i+1] in vocab_set:
                result.append(cur_str[j:i+1])
    return result


print(separate_str("thedogbarks", ["dog", "the", "away", "barks", "he"]))

'''
	•	DP Table (dp): dp[i] represents the segmentation of the substring cur_str[:i] (i.e., the first i characters) that results in valid words from the vocabulary.
 	•	Base Case: An empty substring (cur_str[:0]) has no segmentation, so dp[0] = [].
	•	Transition: For every index i, iterate backward over all possible starting points j of the substring cur_str[j:i]:
	•	If cur_str[j:i] is in the vocabulary and dp[j] is valid, then dp[i] = dp[j] + [cur_str[j:i]].
 

 
 
	•	For each index i, the algorithm looks at all possible substrings ending at i. It checks both:
	•	Whether the substring is valid.
	•	Whether the earlier segment (dp[j]) is valid.
 
 
 dp = [[], None, None, None, None, None, None, None, None, None, None, None]
 	2.	Start filling dp:
	•	For i = 3: cur_str[:3] = "the"
	•	Substring "the" is in the vocabulary. Update dp[3] = dp[0] + ["the"] = ["the"].
	•	For i = 6: cur_str[:6] = "thedog"
	•	Substring "dog" is in the vocabulary. Update dp[6] = dp[3] + ["dog"] = ["the", "dog"].
	•	For i = 11: cur_str[:11] = "thedogbarks"
	•	Substring "barks" is in the vocabulary. Update dp[11] = dp[6] + ["barks"] = ["the", "dog", "barks"].
'''


def separate_str(cur_str, vocabulary):

    vocab_set = set(vocabulary)  # Use a set for fast lookups
    n = len(cur_str)
    dp = [None] * (n + 1)  # dp[i] stores the segmentation of cur_str[:i]
    dp[0] = []  # Base case: empty string has no words

    for i in range(1, n + 1):  # i represents the end of the substring
        for j in range(i):  # j represents the start of the substring
            if cur_str[j:i] in vocab_set and dp[j] is not None:
                dp[i] = dp[j] + [cur_str[j:i]]
                break  # No need to check further; we found a valid segmentation

    return dp[n]  # Return the segmentation for the entire string


vocabulary = ["dog", "the", "away", "barks"]
print(separate_str("thedogbarks", ["dog", "the", "away", "barks", "he"]))


'''backtrack solution
Key Concepts:
	•	Recursive Function: Use recursion to explore all possible segmentations.
	•	Backtracking: If a path doesn’t lead to a valid segmentation, backtrack and try the next possible word.
	•	Base Case: When the string is fully segmented, add the result to the output.
'''


def separate_str_backtrack(cur_str, vocabulary):
    vocab_set = set(vocabulary)  # Convert vocabulary to a set for fast lookup
    result = []

    def backtrack(start, path):
        # Base case: If we've processed the entire string
        if start == len(cur_str):
            result.append(path[:])  # Add a copy of the path to results
            return

        # Try every possible substring starting from `start`
        for end in range(start + 1, len(cur_str) + 1):
            word = cur_str[start:end]
            if word in vocab_set:
                # Choose the word and recurse
                path.append(word)
                backtrack(end, path)
                path.pop()  # backtrack
    backtrack(0, [])
    return result


print(separate_str("thedogbarks", ["dog", "the", "away", "barks", "he"]))
