'''
0表示海洋， 1表示陆地
a[i][j]==1，上下左右也是1时认为是一片陆地
判断所给矩阵包含多少片陆地
'''
def solution(matrix):
	if not matrix or not matrix[0]:
		return 0
	row, col = len(matrix), len(matrix[0])
	count = 0
	for i in range(row):
		for j in range(col):
			if matrix[i][j] == "1":
				count += 1
				dfs(matrix, i, j)

	for i in range(row):
		for j in range(col):
			if matrix[i][j] == "#":
				matrix[i][j] = "1"
    return count

def dfs(matrix, i, j):
	lst = [[1,0],[-1,0],[0,1],[0,-1]]
	if 0<=i<len(matrix) and 0<=j<len(matrix[0]) and matrix[i][j]=="1":
		matrix[i][j] = "#"
		for i in range(4):
			dfs(matrix, i+lst[i][0], j+lst[i][1])