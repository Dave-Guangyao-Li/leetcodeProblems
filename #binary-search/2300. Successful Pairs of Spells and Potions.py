'''
2300. Successful Pairs of Spells and Potions
Solved
Medium
Topics
Companies
Hint
You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.

You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.

 

Example 1:

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
Example 2:

Input: spells = [3,1,2], potions = [8,5,8], success = 16
Output: [2,0,2]
Explanation:
- 0th spell: 3 * [8,5,8] = [24,15,24]. 2 pairs are successful.
- 1st spell: 1 * [8,5,8] = [8,5,8]. 0 pairs are successful. 
- 2nd spell: 2 * [8,5,8] = [16,10,16]. 2 pairs are successful. 
Thus, [2,0,2] is returned.
 

Constraints:

n == spells.length
m == potions.length
1 <= n, m <= 105
1 <= spells[i], potions[i] <= 105
1 <= success <= 1010

Seen this question in a real interview before?
1/5
Yes
No
Accepted
193K
Submissions
435.7K
Acceptance Rate
44.3%
Topics
Array
Two Pointers
Binary Search
Sorting
'''



from bisect import bisect_left
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # Step 1: Sort the potions array for binary search
        potions.sort()
        n = len(potions)
        result = []

        #helper function: Custom binary search to find the first potion >= min_potion
        def binary_search_left(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        # Step 2: Iterate through each spell
        for spell in spells:
            # Step 3: Calculate the minimum potion needed
            # We need potion >= success / spell
            min_potion = (success + spell - 1) // spell # Avoid floating-point division (ceil(success / spell))

            # Step 4: Use binary search to find the first potion that satisfies the condition
            # idx = bisect_left(potions, min_potion)
            idx = binary_search_left(potions, min_potion)
            # Step 5: Count successful potions
            successful_count = n - idx
            result.append(successful_count)

        return result
        

'''
To solve this problem efficiently:
	1.	The key is to reduce the number of pairwise multiplications by leveraging sorting and binary search.
	2.	For each spell, we determine the smallest potion strength that can form a successful pair using binary search.



Binary search works well because:
	1.	Once the potions array is sorted, the condition for success ( \text{spell} \times \text{potion} \geq \text{success} ) becomes monotonic:
	•	Larger potions are more likely to succeed as  \text{spell}  increases.
	2.	This allows us to efficiently find the smallest potion that satisfies the condition for a given spell.



	1.	Sort the potions array:
	•	Sorting ensures that for any spell, once we find the smallest potion that satisfies the condition, all subsequent potions will also satisfy it.
	2.	Iterate through each spell:
	•	For each spell, compute the minimum potion strength required to meet the success condition: potion >= success / spell
    •	Use binary search to find the first potion that satisfies this condition.

	3.	Count the successful pairs:
	•	Subtract the binary search index from the total number of potions to determine how many potions satisfy the condition.
	4.	Store the result for each spell.



    Time Complexity:
	1.	Sorting the potions array:  O(m \log m) , where  m  is the number of potions.
	2.	For each spell, binary search takes  O(\log m) .
	3.	Total:  O(m \log m + n \log m) , where  n  is the number of spells.

Space Complexity:
	•	Sorting takes  O(m)  space (for the sorted array), and the result list takes  O(n) .
	•	Total:  O(m + n) .



    The bisect_left function in Python’s bisect module finds the first position in a sorted array where a value can be inserted while maintaining the array’s sorted order. Specifically:
	•	Input:
	•	potions: A sorted list.
	•	min_potion: The target value to find the position for.
	•	Output:
	•	The index of the first element in potions that is greater than or equal to min_potion.

    potions = [1, 2, 3, 4, 5]
    min_potion = 3
    idx = bisect_left(potions, min_potion)
    print(idx)  # Output: 2
'''