# Intuition
# <!-- Describe your first thoughts / brute force way on how to solve this problem. -->
# We will need to loop through the list, maintain a maxCount variable
# add to maxCount if the value currently is the same as next value
# then after every loop we will compare count to maxCount
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

def longest_streak(head):
    if head is None:
        return 0

    count = 0
    maxCount = 0
    current = head
    lastSeen = head.val
  
    while current is not None:
        if current.val == lastSeen:
            count += 1
        else:
            count = 1

        maxCount = max(count, maxCount)
        lastSeen = current.val
        current = current.next

    return maxCount
