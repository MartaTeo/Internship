# Python3 implementation to print the sequence
# of burning of nodes of a binary tree
 
# A Tree node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# Utility function to create a new node
def new_node(key):
    temp = Node(key)
    return temp
 
# Utility function to print the sequence of burning nodes
def burn_tree_util(root, target, q):
    # Base condition
    if root is None:
        return 0
 
    # Condition to check whether target
    # node is found or not in a tree
    if root.key == target:
        print(root.key)
        if root.left is not None:
            q.append(root.left)
        if root.right is not None:
            q.append(root.right)
 
        # Return statements to prevent
        # further function calls
        return 1
 
    a = burn_tree_util(root.left, target, q)
 
    if a == 1:
        q_size = len(q)
 
        # Run while loop until size of queue
        # becomes zero
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp.key, end=", ")
            del q[0]
 
            # Check if condition for left subtree
            if temp.left is not None:
                q.append(temp.left)
 
            # Check if condition for right subtree
            if temp.right is not None:
                q.append(temp.right)
 
            q_size -= 1
 
        if root.right is not None:
            q.append(root.right)
 
        print(root.key)
 
        # Return statement it prevents further
        # further function call
        return 1
 
    b = burn_tree_util(root.right, target, q)
 
    if b == 1:
        q_size = len(q)
        # Run while loop until size of queue
        # becomes zero
 
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp.key, end=", ")
            del q[0]
 
            # Check if condition for left subtree
            if temp.left is not None:
                q.append(temp.left)
 
            # Check if condition for left subtree
            if temp.right is not None:
                q.append(temp.right)
 
            q_size -= 1
 
        if root.left is not None:
            q.append(root.left)
 
        print(root.key)
 
        # Return statement it prevents further
        # further function call
        return 1
 
# Function will print the sequence of burning nodes
def burn_tree(root, target):
    q = []
 
    # Function call
    burn_tree_util(root, target, q)
 
    # While loop runs unless queue becomes empty
    while q:
        q_size = len(q)
        while q_size:
            temp = q[0]
 
            # Printing of burning nodes
            print(temp.key, end="")
            # Insert left child in a queue, if exist
            if temp.left is not None:
                q.append(temp.left)
            # Insert right child in a queue, if exist
            if temp.right is not None:
                q.append(temp.right)
 
            if len(q) != 1:
                print(", ", end="")
 
            del q[0]
            q_size -= 1
        print()
 
# Driver Code
if __name__ == "__main__":
    """
            10
           /  \
          12  13
              / \
             14 15
            / \ / \
          21 22 23 24
 
        Let us create Binary Tree as shown
        above
    """
    root = new_node(10)
    root.left = new_node(12)
    root.right = new_node(13)
    root.right.left = new_node(14)
    root.right.right = new_node(15)
    root.right.left.left = new_node(21)
    root.right.left.right = new_node(22)
    root.right.right.left = new_node(23)
    root.right.right.right = new_node(24)
 
    burn_tree(root, 14)
# This code is contributed by Potta Lokesh