# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# since the list is nonempty and we want unique vals we can just compare every value in the list with head.val
# if the current.val isnt head.val return False
# else traverse whole list and return true
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

def is_univalue_list(head):
    current = head
    while current is not None:
        if current.val != head.val:
            return False
        current = current.next
    return True
    
  
