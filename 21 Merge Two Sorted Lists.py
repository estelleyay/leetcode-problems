
#  Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode) ->ListNode:

        result = ListNode()
        current = result
        tempNode = None
        while list1 != None and list2 != None:
            tempNode = ListNode()
            if list1.val < list2.val:
                tempNode.val = list1.val
                list1 = list1.next
            else:
                tempNode.val = list2.val
                list2 = list2.next
            current.next = tempNode
            current = tempNode

        if list1 != None:
            current.next = list1
        elif list2 != None:
            current.next = list2
        result = result.next

        return result
