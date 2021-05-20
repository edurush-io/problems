#!/usr/bin/env python3

"""
Given an n x n 2D matrix, rotate the matrix by 90 degrees (clockwise) and in place (not using additional array)
example:
[
    [1, 2],
    [3, 4]
]
rotates to
[
    [3, 1],
    [4, 2]
]
"""

my_arr1 = [
	[1, 2],
	[3, 4]
]

my_arr2 = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
]

my_arr3 = [
	[1,2,3,4],
	[5,6,7,8],
	[9,10,11,12],
	[13,14,15,16]
]


def print_arr(arr):
	for i in range(len(arr)):
		for j in range(len(arr[i])):
			print (arr[i][j], end=" ")
		print()

# the function below can rotate both clockwise and counterclockwise depending on the arugment provided
# clockwise is the default
def rotate_arr_90(arr, s = "clockwise"):
	max_h = len(arr[0]) - 1
	max_v = len(arr) - 1
	
	cnt = 0
	while cnt < max_h:
		i = cnt
		while i < max_h: # variables a,b,c,d used to illustrate the rotation, if we were to optimize we can use just one variable 
			a = arr[cnt][i]
			b = arr[i][max_h-cnt]
			c = arr[max_h-cnt][max_h-i]
			d = arr[max_h-i][cnt]
			
			if s == "clockwise":
				arr[cnt][i] = d
				arr[i][max_h-cnt] = a
				arr[max_h-cnt][max_h-i] = b
				arr[max_h-i][cnt] = c
			else:
				arr[cnt][i] = b
				arr[i][max_h-cnt] = c
				arr[max_h-cnt][max_h-i] = d
				arr[max_h-i][cnt] = a
			i += 1
		cnt += 1
	return arr

if __name__ == "__main__":
	print ("Initial array")
	print_arr(my_arr1)
	print ("Rotated array")
	print_arr(rotate_arr_90(my_arr1, "clockwise"))

	print ("Initial array")
	print_arr(my_arr2)
	print ("Rotated array")
	print_arr(rotate_arr_90(my_arr2))

	print ("Initial array")
	print_arr(my_arr3)
	print ("Rotated array")
	print_arr(rotate_arr_90(my_arr3, "counterclockwise"))
