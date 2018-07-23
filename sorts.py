def bubble_sort(arr):
	sorted=False
	while not sorted:
		sorted = True
		for e in (e for e in range(len(arr)-1) if arr[e] > arr[e+1]):
			sorted = False
			arr[e], arr[e+1] = arr[e+1], arr[e]
	return arr

#############################################################

def merge(arr1, arr2):
	new_arr = []
	while len(arr1) > 0 and len(arr2) > 0:
		if arr1[0] < arr2[0]: new_arr.append(arr1.pop(0))
		else: new_arr.append(arr2.pop(0))
	return new_arr + arr1 + arr2

def merge_sort(arr):
	if len(arr) == 1: return arr
	return merge(merge_sort(arr[:len(arr)//2]), merge_sort(arr[len(arr)//2:]))

#############################################################

def quick_sort(arr):
	if len(arr) <= 1: return arr
	pivot = arr.pop(0)
	left = [num for num in arr if num < pivot]
	right = [num for num in arr if num >= pivot]
	return quick_sort(left) + [pivot] + quick_sort(right)
  
#############################################################

def sel_sort(arr):
	length = len(arr)
	while length > 0:
		max_i = 0
		for i in range(length):
			if arr[i] > arr[max_i]: max_i = i
		arr[max_i], arr[length-1] = arr[length-1], arr[max_i]
		length -= 1
	return arr





print('merge:', merge_sort([1,7,2,6,8,4,1,6,6,-4,2,0,-67]))
print('quick:', quick_sort([6,5,7,9,3,6,-13,2,-6]))
print('bubble:', bubble_sort([6,5,7,9,3,6,-13,2,-6]))
print('selection:', sel_sort([6,5,7,9,3,6,-13,2,-6]))