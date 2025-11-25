# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# loop through both lists at the same time while both heads don't equal nulll
#  maintain count of what node you're on, odd would be 1 even would be 2
# based on this we know what to do, 
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

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
#     self.next = None


def zipper_lists(head_1, head_2):
  tail = head_1
  c1 = head_1.next
  c2 = head_2
  count = 0
  while c1 is not None and c2 is not None:
    if count % 2 == 0:
      tail.next = c2
      c2 = c2.next
    else:
      tail.next = c1
      c1 = c1.next
    tail = tail.next
    count += 1
    
  if c1 is not None:
    tail.next = c1
  if c2 is not None:
    tail.next = c2
    
  return head_1