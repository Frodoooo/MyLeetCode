class ListNode:
    def __init__(self, val=0, next = None):
         self.val = val
         self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre =  dummy_node
        cur = pre.next
        i = 0
        while (cur != None):
            section_head = cur
            for j in range(k - 1):
                cur = cur.next
                if(cur == None):return dummy_node.next
            section_end = cur

            pre.next = self.reverseBetween(section_head,0,k - 1)
            pre = section_head
            cur = pre.next
            i += 1
        return dummy_node.next



    def reverseBetween(self, head: ListNode, left: int, right) -> ListNode:
        dummy_node = ListNode(-1)
        dummy_node.next = head
        pre = dummy_node
        for _ in range(left - 1):
            pre = pre.next

        cur = pre.next
        for _ in range(right - left):
            next = cur.next
            cur.next = next.next
            next.next = pre.next
            pre.next = next
        return dummy_node.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
mySolution = Solution()
newhead = mySolution.reverseKGroup(node1,2)
cur = newhead
res = []
for i in range(5):
    res.append(cur.val)
    print(res)
    cur = cur.next
print(res)

