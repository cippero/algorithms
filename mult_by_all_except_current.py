# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

# Follow-up: what if you can't use division?

def multByAllExceptCurrent(temp_arr, element):
  product = 1
  for j in temp_arr:
    if j != element: product *= j
  return product

def multArr (arr):
  newArr = [1] * len(arr)
  for i in range(len(newArr)):
    newArr[i] = multByAllExceptCurrent(arr, arr[i])
  print(newArr)

multArr([1,2,3,4,5]);