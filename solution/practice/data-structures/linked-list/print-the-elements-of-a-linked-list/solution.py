# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    if head == None:
        return;
    n = head
    while(n != None):
        print(n.data)
        n = n.next