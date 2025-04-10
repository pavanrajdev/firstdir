class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insertion in BST
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# A. Inorder Traversal (Left, Root, Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)

# B. Preorder Traversal (Root, Left, Right)
def preorder(root):
    if root:
        print(root.val, end=' ')
        preorder(root.left)
        preorder(root.right)

# C. Postorder Traversal (Left, Right, Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val, end=' ')

# D. Level Order Traversal (BFS)
from collections import deque
def levelOrder(root):
    if root is None:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Example Usage
if __name__ == "__main__":
    root = None
    for key in [50, 30, 70, 20, 40, 60, 80]:
        root = insert(root, key)

    print("Inorder traversal:")
    inorder(root)
    print("\nPreorder traversal:")
    preorder(root)
    print("\nPostorder traversal:")
    postorder(root)
    print("\nLevel order traversal:")
    levelOrder(root)
