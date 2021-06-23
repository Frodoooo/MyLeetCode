class Solution(object):
    def __init__(self):
        self.successor = None

    def reverseListN(self,head,n):
        if(n == 1):
            self.successor = head.next
            return head

        p = self.reverseListN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return p

    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if(left == 1):
            return self.reverseListN(head,right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head
