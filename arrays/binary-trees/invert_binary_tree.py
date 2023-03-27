# Wrtie a function that takes in a Binary Tree and inverts it. In other words, the function should swap every left node in the tree for its corresponding right node.

# Each BinaryTree node has an integer value, a left child node, and a right child node. Children nodes can either be BinaryTree nodes themselves or None / null.

#                      1
#                  /       \
#                 2         3
#              /    \    /    \
#             4      5  6      7
#           /  \ 
#          8   9

def invertBinaryTree(tree):
  if tree is None:
    return
  swapLeftAndRightNodes(tree)
  invertBinaryTree(tree.left)
  invertBinaryTree(tree.right)
  
  
  
def swapLeftAndRightNodes(tree):
  tree.left, tree.right = tree.right, tree.left