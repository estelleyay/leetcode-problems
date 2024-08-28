# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        # iterative method: using a stack
        stack = []
        if head != None:
            stack.append(head.val)
            while head.next != None:
                stack.append(head.next.val)
                head = head.next
                #print(head.val)
            n = len(stack)
            temp = head
            while n > 0:
                temp.next = ListNode(stack.pop(),None)
                temp = temp.next
                #print(temp.val)
                n -= 1
            return head.next
