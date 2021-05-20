#!/usr/bin/env python3

"""
Given a non-empty array of digits represented as a non-negative integer, add one to the integer.
- each element of the aray is a single digit
- most significant element is the first element of the array

Examples:
Input: [1, 2, 8]
Output: [1, 2, 9] # 128 + 1 = 129

Input: [9, 9, 9, 9]
Output: [1, 0, 0, 0] # 9999 + 1 = 10000

two sample fucntions

"""

my_arr1 = [1, 2, 8]
my_arr2 = [9, 9, 9, 9]
my_arr3 = [9, 8, 9, 9]
my_arr4 = [7, 8, 9]

def plus_one_like_school (arr): # we'll loop backwards, add 1 to the last element and move left if last element is 9
	for x in range(len(arr)-1, -1, -1):
		if arr[x] != 9:
			arr[x] += 1
			return arr
		else:
			arr[x] = 0
	arr.insert(0,1)
	return arr

def plus_one_using_str_map(arr):
	num = int("".join(map(str, arr)))
	num += 1
	return [int(x) for x in str(num)]

if __name__ == "__main__":
	print (my_arr1, my_arr2, my_arr3, my_arr4)
	print (plus_one_like_school(list(my_arr1)))
	print (plus_one_like_school(list(my_arr2)))
	print (plus_one_like_school(list(my_arr3)))
	print (plus_one_like_school(list(my_arr4)))
	print (plus_one_using_str_map(my_arr1))
	print (plus_one_using_str_map(my_arr2))
	print (plus_one_using_str_map(my_arr3))
	print (plus_one_using_str_map(my_arr4))