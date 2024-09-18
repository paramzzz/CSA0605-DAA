
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplicates(head):
    
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            
            current = current.next
    return head


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(4)

head = deleteDuplicates(head)

while head:
    print(head.val, end=" -> " if head.next else "\n")
    head = head.next
