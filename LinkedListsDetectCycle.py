# https://www.hackerrank.com/challenges/ctci-linked-list-cycle

"""  GIVEN
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
""" END GIVEN


def has_cycle(head):
    if head == None:
        return False
    elif head.next == None:
        return False
    slow = head.next
    fast = head.next.next
    if slow == fast: return True
    has_cycle(head.next)
    
