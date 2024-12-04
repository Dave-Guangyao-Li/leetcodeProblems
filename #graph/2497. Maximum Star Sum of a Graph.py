'''2497. Maximum Star Sum of a Graph
Solved
Medium
Topics
Companies
Hint
There is an undirected graph consisting of n nodes numbered from 0 to n - 1. You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.

You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.

The image below shows star graphs with 3 and 4 neighbors respectively, centered at the blue node.


The star sum is the sum of the values of all the nodes present in the star graph.

Given an integer k, return the maximum star sum of a star graph containing at most k edges.

 

Example 1:


Input: vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2
Output: 16
Explanation: The above diagram represents the input graph.
The star graph with the maximum star sum is denoted by blue. It is centered at 3 and includes its neighbors 1 and 4.
It can be shown it is not possible to get a star graph with a sum greater than 16.
Example 2:

Input: vals = [-5], edges = [], k = 0
Output: -5
Explanation: There is only one possible star graph, which is node 0 itself.
Hence, we return -5.
 

Constraints:

n == vals.length
1 <= n <= 105
-104 <= vals[i] <= 104
0 <= edges.length <= min(n * (n - 1) / 2, 105)
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
0 <= k <= n - 1

Seen this question in a real interview before?
1/5
Yes
No
Accepted
23.2K
Submissions
57.7K
Acceptance Rate
40.1%
Topics
Array
Greedy
Graph
Sorting
Heap (Priority Queue)'''

from collections import defaultdict
from typing import List


class Solution:
    def maxStarSum(self, values: List[int], edges: List[List[int]], k: int) -> int:
        # Create a graph represented as an adjacency list
        graph = defaultdict(list)

        # Iterate over each edge and build an adjacency list for nodes with positive values
        for node_a, node_b in edges:
            if values[node_b] > 0:
                graph[node_a].append(values[node_b])
            if values[node_a] > 0:
                graph[node_b].append(values[node_a])

        # Sort the adjacency lists in descending order to prioritize larger values
        for neighbors in graph.values():
            neighbors.sort(reverse=True)

        # Calculate the maximum star sum by adding the node's value to the
        # sum of up to k highest values among its adjacent nodes
        max_star_sum = max(value + sum(graph[node_index][:k])
                           for node_index, value in enumerate(values))

        # Return the maximum star sum found
        return max_star_sum


'''
https://algo.monster/liteproblems/2497
The problem describes an undirected graph with n nodes numbered from 0 to n-1. Each node has an associated value defined in the array vals, where vals[i] represents the value of the ith node. Additionally, we are given a list of undirected edges defined in the array edges. An edge connects two nodes, implying that the nodes are directly reachable from each other.

A star graph is a specific type of subgraph in which one central node is connected to some or all other nodes through edges, but those other nodes are not connected to each other. The star sum is the combined value of the nodes in this subgraph, including the central node and its neighbors.

The task is to find the maximum star sum possible by including at most k edges in the star graph. In other words, what is the highest sum of node values we can achieve when we select a subset of the graph that forms a star graph, with the central node having up to k neighbors.




To find the maximum star sum, we should aim to include the nodes with the highest values adjacent to our chosen central node. Since the edges are undirected, we need to consider each node as a potential center of the star graph and calculate the maximum sum obtainable with it as the center.

The given solution follows these steps:

Create an adjacency list, g, using defaultdict(list) from Python's collections module, to store the nodes (a) and their corresponding connected nodes' values (vals[b]) if their value is greater than zero.

For all edges (a, b), do the following:

If vals[b] is positive, append it to g[a] (connected nodes' values for a).
Conversely, if vals[a] is positive, append it to g[b].
Sort the lists of connected nodes' values in descending order for each node in g. It ensures that the highest valued neighbor is considered first.

Calculate the star sum for each node as the sum of its value, v, and the sum of at most k highest valued neighbors from the respective list in g. This is accomplished by iterating through all nodes enumerated along with their values (enumerate(vals)) and computing the sum of a node's value and the total of its k highest connected nodes' values.

Finally, the maxStarSum function returns the maximum star sum obtained from all possible center nodes.



Creating Adjacency List (Undirected): Our adjacency list g would be built as follows by iterating over the edges:

g[0] -> [2, 3, 4]    # Node 0 is connected to nodes 1, 2, 3 with positive values
g[1] -> [1, 5]       # Node 1 is connected to nodes 0 and 4
g[2] -> [1, 5]       # Node 2 is connected to nodes 0 and 4
g[3] -> [1]          # Node 3 is connected to node 0
g[4] -> [2, 3]       # Node 4 is connected to nodes 1 and 2
Sorting Neighbors' Values: The next step is to sort each list of connected nodes' values in descending order:

g[0] -> [4, 3, 2]    # Sort 2, 3, 4 in descending order
g[1] -> [5, 1]       # Sort 1, 5 in descending order
g[2] -> [5, 1]       # Sort 1, 5 in descending order
g[3] -> [1]          # Already sorted since there's just one element
g[4] -> [3, 2]       # Sort 2, 3 in descending order
Calculating Star Sum: Now, for each node, we will calculate the star sum by taking its value and adding the sum of its k highest valued neighbors:

For node 0: Star sum = 1 + (4+3) = 8 (Take the 2 highest values 4 and 3)
For node 1: Star sum = 2 + (5) = 7 (Only 1 neighbor's value can be taken since k=2 and node 1's value has to be included)
For node 2: Star sum = 3 + (5) = 8 
For node 3: Star sum = 4 + (1) = 5 
For node 4: Star sum = 5 + (3) = 8 (Same reasoning as node 1)
Note that we only include up to k neighbor's values, which is why even though node 0 has three neighbors, only the highest two (4 and 3) are included in the sum.

Finding the Maximum Star Sum: The final step is to find the maximum star sum possible:

Maximum Star Sum = max(8, 7, 8, 5, 8) = 8
'''
