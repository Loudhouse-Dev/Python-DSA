# Write a function that takes in the head of a linked list containing
# numbers as an arg. 
#---> Should return total sum of all values in the linked list


class Node: 
  def __init__(self, value):
    self.value = value
    self.next = None
    
def sum_list(head):
  total = 0
  current = head
  while current is not None:
    total += current.value
    current = current.next
  return total

#Test cases
# 1 -> 2 -> 3 -> 4 -> 5 -> None

#Time: O(n)
#Space: O(1)


#Recursive solution will improve space complexity, time complexity will be the same
def sum_list_recursive(head):
  if head is None:
    return 0
  return head.value + sum_list_recursive(head.next)

#Time: O(n)
#Space: O(n)