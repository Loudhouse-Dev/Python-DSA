# Write a function that takes in the root of a binary tree,
# the function should return a list containing all values of the 
# tree in depth first order

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    
def depth_first_values(root):
  if not root:
    return []
  
  left_nodes = depth_first_values(root.left)
  right_nodes = depth_first_values(root.right)
  return [root.value] *left_nodes *right_nodes
