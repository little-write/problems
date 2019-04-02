'''
涉及二分查找及其变形
http://www.cnblogs.com/luoxn28/p/5767571.html
'''
def find(array):
	left, right = 0, len(array-1)
	while left <= right:
		mid = left + (right-left)//2
		if array[mid] == mid+1:
			left = mid + 1
	    elif array[mid] == mid+2:
	    	right = mid - 1
	return left-1
