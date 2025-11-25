# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  pass # todo
  current = head
  sum = 0
  while current != None:
    sum += current.val
    current = current.next
  return sum
    