# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Brute Force:
"""
-create an array with all the nodes
-now make two pointers from each end i and j
-connect i to j
-i += 1
-connect j to i
-j -= 1
-connect i to none
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #setting up fast and slow pointers:
        slow, fast = head, head.next
        #setting up their positions, slow at halfway and fast at end:
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #setup a second list which starts from halfway and reverse it:
        second = slow.next
        #setup the new end node(pointing to none now) as prev
        prev = slow.next = None
        #reverse linked list
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        #start the two lists each from their heads:
        first, second = head, prev
        #combine first list and second list
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
















