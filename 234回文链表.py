class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        #快慢指针法
        slow = head
        quick = head
        while(quick != None and quick.next != None):
            slow = slow.next
            quick = quick.next.next
        #如果长度为奇数，quick没有指向None，则slow再往前一步
        if (quick != None):
            slow = slow.next

        #从slow开始反转后面的链表
        left = head
        dummy_node = None
        while(slow != None):
            nxt = slow.next
            slow.next = dummy_node
            dummy_node = slow
            slow = nxt
        right = dummy_node
        while(right != None):
            if(left.val != right.val):
                return False
            left = left.next
            right = right.next
        return True

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

mySolution = Solution()
print(mySolution.isPalindrome(node1))
