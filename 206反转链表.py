class Solution(object):
    def reverseList(self,head):
        if(head == None or head.next == None):
            return head
        if(head.next != None):
            p = self.reverseList(head.next)
            head.next.next = head
            head.next = None
            return p




