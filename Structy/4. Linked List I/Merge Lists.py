# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# Keep a tail, count, c1 / c2 variables
# loop through the lists and check for which one has the smaller number at the current node
# whichever one has the smaller node will move onto the tail
#
# Final Approach
# <!-- Describe your approach to solving the problem. -->
#
#
# Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $O(n)$$ -->
#
# - Space complexity:
# <!-- Add your space complexity here, e.g. $O(n)$$ -->
#
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  pass # todo
  dummyHead = Node(None)
  tail = dummyHead
  c1 = head_1
  c2 = head_2
  
  while c1 is not None and c2 is not None:
      if c1.val > c2.val:
          tail.next = c2
          c2 = c2.next
      else:
          tail.next = c1
          c1 = c1.next
      tail = tail.next

  if c1 is not None: tail.next = c1
  if c2 is not None: tail.next = c2

  return dummyHead.next

