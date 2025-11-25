class Node:
  def __init__(self, val):
    self.val = val
    self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
a.next = b
b.next = c
c.next = d

# A -> B -> C -> D -> None
# iterative
def print_list(head):
  curr = head
  while curr is not None:
    print(curr.val)
    curr = curr.next


# recursive

def printList(head):
  if head is None:
    return
  print(head.val)
  return printList(head.next)



print_list(a)
printList(a)