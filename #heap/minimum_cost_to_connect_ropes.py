# You're preparing for a tug-of-war competition and have several ropes of different lengths. To get the optimal length, you need to connect these ropes into one. Connecting two ropes of lengths `a` and `b` costs `a + b`. Return the minimum total cost to connect all ropes into one.


import heapq
def min_cost_connect(ropes):
    # lengths `a` and `b` costs `a + b`
    # [1,2,3] -> 1+2=3 3+3=6 total 3+6 = 9 , 3+2=5 5+1= 6 total 11
    # If no ropes or just one rope, no cost to connect
    if not ropes:
        return 0
    if len(ropes) == 1:
        return 0  # No cost to connect one rope
    # Step 1: Convert the list into a min-heap
    heapq.heapify(ropes)
    # Step 2: Initialize total cost
    total_cost = 0

    # Step 3: Combine ropes until only one rope remains
    while len(ropes) > 1:
        # Extract the two smallest ropes
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)

        # Combine them and calculate the cost
        combined = first + second
        total_cost += combined

        # Add the combined rope back to the heap
        heapq.heappush(ropes, combined)
    # Step 4: Return the total cost
    return total_cost


print(min_cost_connect([1,2,3,4,5]))
'''
Step 1: Problem Breakdown
	•	If we connect two ropes of lengths a and b, the cost is a + b.
	•	To minimize the total cost, always combine the two shortest ropes first (greedy approach).
	•	Repeat this process until there’s only one rope left.

Using a min-heap allows efficient extraction of the smallest two ropes at each step.


	1.	heapify(ropes): Converts the list into a heap in O(n) time.
	2.	heappop(): Extracts the smallest element in O(\log n).
	3.	heappush(): Inserts a new element into the heap in O(\log n).




    	1.	Input: [1, 2, 3, 4, 5]
Output: 33
	2.	Input: [5, 10, 15]
Output: 45
	3.	Input: [1, 2, 3]
Output: 9
	4.	Input: [1, 1, 1, 1]
Output: 8
	5.	Input: [8, 4, 6, 12]
Output: 58
	6.	Input: [20, 4, 8, 2]
Output: 54
	7.	Input: [100]
Output: 0
	8.	Input: []
Output: 0
'''