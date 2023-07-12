# H1: Questions of technical interview "Binary Tree"


Question: give me simple code in python for depthfirstvalues in datastrucutre and algorithm for tree construction
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_values(root):
    # List to store the values of nodes visited
    values = []
    
    # Define a helper function for the DFS traversal
    def dfs(node):
        if node is None:
            return
        values.append(node.value)  # visit the node
        dfs(node.left)  # visit left child
        dfs(node.right)  # visit right child

    dfs(root)
    
    # return list of values of nodes visited in DFS manner
    return values

Question: you can also implement Depth-First Search (DFS) iteratively using a stack. Here's how you can do it:
In this code, depth_first_values(root) is a recursive function that returns a list of the node values obtained by a DFS traversal of the tree rooted at root. If root is None (indicating an empty tree), it returns an empty list. Otherwise, it recursively gets the DFS node values for the left and right subtrees, and returns a list consisting of the root value followed by the values in the left and right subtrees. This ensures that the nodes are visited in the order: root, left subtree, right subtree.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth_first_values(root):
    if root is None:
        return []

    values = []
    stack = [root]

    while stack:
        node = stack.pop()
        values.append(node.value)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return values

Question: breath-first-search 

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def breadth_first_values(root):
    if root is None:
        return []

    values, queue = [], deque([root])
    
    while queue:
        node = queue.popleft()
        values.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return values

Theory:  

In this code, breadth_first_values(root) is a function that performs a BFS on a binary tree. It uses a queue (implemented with collections.deque) to keep track of nodes to visit. We start by adding the root node to the queue.

In each iteration of the while loop, we remove a node from the front of the queue (queue.popleft()), add its value to the values list, and then add its children (if any) to the end of the queue. We continue this process until the queue is empty, i.e., we've visited all nodes.

This approach ensures that nodes are visited level by level, from left to right within each level, as required by the BFS algorithm.


Question:solve me a recursive tree sum function in python and explain

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0
    
    left_sum = tree_sum(root.left)
    right_sum = tree_sum(root.right)
    
    return root.value + left_sum + right_sum

Theory:
In this code, tree_sum(root) is a recursive function that calculates the sum of all nodes in the binary tree rooted at root.

If root is None (indicating an empty tree), it returns 0. Otherwise, it recursively calculates the sum of all nodes in the left and right subtrees, and then returns the sum of the root's value, the left subtree sum, and the right subtree sum. This ensures that the values of all nodes in the tree are included in the sum.

The time complexity for this function is O(N), where N is the number of nodes in the tree, because each node is visited exactly once.

Question: solve this problem by using a queue 

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_sum(root):
    if root is None:
        return 0

    queue = deque([root])
    total = 0
    
    while queue:
        node = queue.popleft()
        total += node.value
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return total
In this code, tree_sum(root) is a function that performs a BFS on a binary tree. We start by adding the root node to the queue. In each iteration of the while loop, we remove a node from the front of the queue (queue.popleft()), add its value to the total sum, and then add its children (if any) to the end of the queue. This process continues until the queue is empty, i.e., we've visited all nodes.

This approach ensures that nodes are visited level by level, from left to right within each level, as required by the BFS algorithm.

question: tree min value in python

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_min(root):
    if root is None:
        return float('inf')  # Return infinity if tree is empty
    
    left_min = tree_min(root.left)  # Minimum value in left subtree
    right_min = tree_min(root.right)  # Minimum value in right subtree
    
    return min(root.value, left_min, right_min)  # Return the minimum value

In this code, tree_min(root) is a recursive function that returns the minimum value in the binary tree rooted at root. If root is None (indicating an empty tree), it returns infinity. Otherwise, it recursively finds the minimum value in the left and right subtrees, and then returns the minimum of the root's value, the left subtree minimum, and the right subtree minimum.

This ensures that all nodes in the tree are considered when determining the minimum value. The time complexity of this function is O(N), where N is the number of nodes in the tree, because each node is visited exactly once.


Question: iteratively:

Sure, you can find the minimum value in a binary tree using an iterative approach as well. We'll again use a breadth-first search (BFS) approach with a queue for this. Here's how to do it:

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_min(root):
    if root is None:
        return None

    queue = deque([root])
    min_val = float('inf')
    
    while queue:
        node = queue.popleft()
        min_val = min(min_val, node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return min_val

In this code, tree_min(root) is a function that performs a BFS on a binary tree. We start by adding the root node to the queue. In each iteration of the while loop, we remove a node from the front of the queue (queue.popleft()), update min_val if the current node's value is less than min_val, and then add its children (if any) to the end of the queue. This process continues until the queue is empty, i.e., we've visited all nodes.

This approach ensures that nodes are visited level by level, from left to right within each level. The minimum value is updated in each iteration, ensuring that the minimum value of all nodes in the tree is found. The time complexity of this function is O(N), where N is the number of nodes in the tree, as each node is visited exactly once.




