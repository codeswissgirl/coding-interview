"""
       1. question: 
        - binary search tree: ascendance roder left smaller than node, right bigger than node
        - quaranteed that the number is existing
        2. problem statemtent: approach
        we have here an binary seraach tree whereas we have to insert a value in our tree. we dont have to check balance tree bc is done. so i assume that we would urn this in Space O(longn) 
        - recurisve appraoch 
        - iterative 
        start from root
        traverse the tre to find the location to insert
        - inerset the new node
        and time. O(n) n is the depth of the tree
        3. pseudo code
        - brute force appraoch: 
        travers into every node: preorder traversal: current - to left and than to right. O(n)
        if val is smaller than 4: we go left
        than we check the children 

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
