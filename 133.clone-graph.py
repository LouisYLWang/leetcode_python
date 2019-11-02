#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        visited = dict()
        def Helper(node, visited):
            if node.val not in visited and node:
                new_node = Node(node.val, list())
                visited[node.val] = new_node
                for node_ in node.neighbors:
                    new_node.neighbors.append(Helper(node_, visited))
                return new_node
            return visited[node.val]
        return Helper(node, visited)
# @lc code=end

