Binary Tree(at most 2 children)


-root has no parent
-every leaf is two edges away from the root.


 

iterative = using stack
# RECURSIVE DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
# ITERATIVE DFS
class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
    def depthfirstvalue(root):
        if root is None: return []
        values=[]
        stack=[root]
        while stack:
            node=stack.pop()
            values.append(node.value)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
        return values
# BFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:q.append(node.left)
                if node.right: q.append(node.right)
            level += 1
        return level

easy implementation: 
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def treesum(root):
    #recursive
    if root is None: return 0
    left_value=treesum(root.left)
    right_value=treesum(root.right)
    return root.value+left_value+right_value

def treesum(root)
    #iterative
    if root is None: return 0
    
    q=deque([root])
    total=0
    while q: 
        curr=q.popleft()
        total+=curr.value
        if curr.left: q.append(curr.left)
        if curr.right: q.append(curr.right)
    return total


