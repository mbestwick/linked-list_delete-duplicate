"""
You're given the pointer to the head node of a sorted linked list, where the
data in the nodes is in ascending order. Delete as few nodes as possible so that
the list does not contain any value more than once. The given head pointer may
be null indicating that the list is empty.

Input Format
You have to complete the Node* RemoveDuplicates(Node* head) method which takes
one argument - the head of the sorted linked list. You should NOT read any input
from stdin/console.

Output Format
Delete as few nodes as possible to ensure that no two nodes have the same data.
Adjust the next pointers to ensure that the remaining nodes form a single sorted
linked list. Then return the head of the sorted updated linked list. Do NOT
print anything to stdout/console.

"""


class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def RemoveDuplicates(head):
    # if null, return null
    if not head:
        return head

    # while curr data = next data, keep moving pointer to next next
    while head.next and head.data == head.next.data:
        head.next = head.next.next

    # once you're pointing to a unique value, recursive call
    head.next = RemoveDuplicates(head.next)

    return head
