def reverse(PHead):
	pre = None
	cur = PHead
	while cur:
		tmp = cur.next
		cur.next = pre
		pre = cur
		cur = tmp
    return pre