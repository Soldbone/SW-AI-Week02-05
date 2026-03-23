# https://leetcode.com/problems/average-of-levels-in-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
### BFS ###
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        from collections import deque

        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_sum / level_size)
        return result


### DFS 1 ###
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        sums = []
        counts = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(sums):
                sums.append(0)
                counts.append(0)
            sums[depth] += node.val
            counts[depth] += 1
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return [sums[i] / counts[i] for i in range(len(sums))]
    

### DFS 2 ###
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(root, level=0, lst=None):
            if lst is None:
                lst = []
            
            if root is None:
                return
            
            if level == len(lst):
                lst.append([])
            
            lst[level].append(root.val)

            dfs(root.left, level + 1, lst)
            dfs(root.right, level + 1, lst)

            if level == 0:
                for i in range(len(lst)):
                    lst[i] = sum(lst[i]) / len(lst[i])
                return lst
        return dfs(root)