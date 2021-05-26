#!/usr/bin/env python3

"""
Given a list of non negative integers, arrange them such that they form the largest number.
Output as string
Examples

Input: [3, 30, 34, 5, 9]
Output: 9534330

Input: [1, 34, 3, 98, 9, 76, 45, 4]
Output: 998764543431

Input: [1, 10, 20]
Output: 20110

Input: [54, 546, 548, 60]
Output: 6054854654

"""

my_arr1 = [3, 30, 34, 5, 9]
my_arr2 = [1, 34, 3, 98, 9, 76, 45, 4]
my_arr3 = [1, 10, 20]
my_arr4 = [54, 546, 548, 60]

def isLarger(a, b):
	ab = str(a) + str(b)
	ba = str(b) + str(a)
	if int(ab) > int(ba):
		return True
	return False

def mySort(arr, start = 0): # custom sorting algorithm
	if start == len(arr):
		return arr
	current_max = arr[start]
	ind = start
	for i in range(start+1, len(arr)):
		if isLarger(arr[i], current_max):
			current_max = arr[i]
			ind = i
	if ind != start:
		a = arr[start]
		arr[start] = current_max
		arr[ind] = a
	return mySort(arr, start + 1)

def maxNum(arr):
	print ("Array: ", arr)
	mySort(arr)
	return "".join(str(i) for i in arr)
if __name__ == "__main__":
	print (maxNum(my_arr1))
	print (maxNum(my_arr2))
	print (maxNum(my_arr3))
	print (maxNum(my_arr4))