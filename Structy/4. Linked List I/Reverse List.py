# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def reverse_list(head):
  pass # todo
  Prev = None
  Current = head
  
  while Current != None:
    Next = Current.next
    Current.next = Prev
    Prev = Current
    Current = Next
  return Prev
    
