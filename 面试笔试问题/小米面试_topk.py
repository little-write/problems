'''快排'''
import random
def top_k(A, k):
	n = len(A)
	if n<=0 or k>n or k<=0:
		return []
    low, high = 0, len(A)-1
	m = _partition(A, low, high)
	while m != k:
		if m > k:
			high = m - 1
			m = _partition(A, low, high)
		else:
			low = m + 1
			m = _partition(A, low, high)
	res = A[:k]
	res.sort()
	return res
def _partition(A, low, high):
	j = low
	if low < high:
		r = random.randint(low, high)
		A[low], A[r] = A[r], A[low]
		pivot = A[low]
		for i in range(low+1, high+1):
			if A[i] > pivot:
				j += 1
				A[i], A[j] = A[j], A[i]
		A[j], A[low] = A[low], A[j]
    return j

'''堆排'''
def top_k(A, k):
	n = len(A)
	if n<=0 or k<=0 or k>n:
		return []
	for i in range((k-1)//2, -1, -1):
		adjustHeap(A, i, k-1)
	for j in range(k, n):
		if A[j] > A[0]:
			A[j], A[0] = A[0], A[j]
			adjustHeap(A, 0, k-1)
	res = A[:k]
	res.sort()
	return res
def adjustHeap(A, i, k):
	while True:
		minPos = i
		if (2*i+1)<=k and A[minPos] > A[(2*i+1)]:
			minPos = 2*i+1
		if (2*i+2)<=k and A[minPos] > A[(2*i+2)]:
			minPos = 2*i+2
		if i==minPos:
			brake
	    A[i], A[minPos] = A[minPos], A[i]
	    i = minPos




