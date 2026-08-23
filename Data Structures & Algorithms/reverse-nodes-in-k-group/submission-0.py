class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        groupPrev = dummy

        while True:

            # Find the kth node
            kth = groupPrev
            for i in range(k):
                kth = kth.next

                if kth is None:
                    return dummy.next

            groupNext = kth.next

            # Reverse the group
            prev = groupNext
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # Connect previous part with reversed group
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp