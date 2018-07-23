#FIX
def binary_search(num, arr, min=0, max=-1):
	if min == max: return -1
	if max == -1: max = len(arr)-1
	mid = len(arr)//2
	if num == arr[mid]: return mid
	if num <= mid: binary_search(num, arr, min, max)
	else: binary_search(num, arr, mid, max)

print('binary search:', binary_search(17, [1,8,2,7,3,13,-24,0,-5,2]))