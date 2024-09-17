import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i))
            lists[i] = l.next
    dummy = ListNode()
    current = dummy
    while min_heap:
        val, idx = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next
        if lists[idx]:
            heapq.heappush(min_heap, (lists[idx].val, idx))
            lists[idx] = lists[idx].next
    return dummy.next
