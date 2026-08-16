class Solution:
    def copyRandomList(self, head):

        old_to_new = {}

        # Step 1: Create all new nodes
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Step 2: Connect next and random pointers
        curr = head

        while curr:
            old_to_new[curr].next = old_to_new.get(curr.next)
            old_to_new[curr].random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new.get(head)