#!/usr/bin/env python3

"""
Compare two version numbers
if version1 is > version2 return 1
if version1 is < version2 return -1
else return 0
Example:
V1 = "2.2.20"
V2 = "2.1.20"
return 1
"""

V1 = "1.0.27"
V2 = "1.0.27.2"

V3 = "2.2.20"
V4 = "2.1.20"

V5 = "3.3.3"
V6 = "3.3.3"

def cmp_ver (s1, s2):
	ret = 0
	if s1 == s2:
		return ret
	arr1 = s1.split(".")
	arr2 = s2.split(".")
	arr1 = [int(i) for i in arr1]
	arr2 = [int(i) for i in arr2]

	i = 0
	l1, l2 = len(arr1), len(arr2)
	if l1>l2:
		min = l2
	else:
		min = l1
	for i in range(min):
		if arr1[i] > arr2[i]:
			return 1
		elif arr1[i] < arr2[i]:
			return -1
		else:
			continue
	if l1 > l2:
		return 1
	elif l2 > l1:
		return -1
	return 0

if __name__ == "__main__":
	print (cmp_ver(V1, V2))
	print (cmp_ver(V3, V4))
	print (cmp_ver(V5, V6))