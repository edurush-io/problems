#!/usr/bin/env python3

"""
Simple stack example in Python
Use case: parse "code" to verify proper opening and closing of brackets
"""

class Stack:
	def __init__ (self):
		self.items = []
	
	def isEmpty(self):
		if self.size() == 0:
			return True
		return False
	
	def push (self, item):
		self.items.append(item)

	def pop (self):
		return self.items.pop()
	
	def read (self):
		return self.items[len(items)-1]
	
	def size (self): 
		return len(self.items)

	def isOpener(self, c):
		if c == '{' or c == '[' or c == '(':
			return True
		return False

	def isCloser(self, c):
		if c == '}' or c == ']' or c == ')':
			return True
		return False
	
	def isMatch(self, c):
		if self.isEmpty():
			return False
		el = self.pop()
		if c == '}' and el == '{':
			return True
		elif c == ']' and el == '[':
			return True
		elif el == '(':
				return True
		return False
	
	def check(self, s):
		for i in s:
			if self.isOpener(i):
				self.push(i)
			elif self.isCloser(i):
				if not self.isMatch(i):
					print ("Missmatch closing " + i)
					return False
		if self.isEmpty():
			return True
		else:
			print ("Not closed opener")
			return False
				

s1 = "(var a = 1; var b = {x: [1, 2, 3]}, c = {y: 'one', 'two', 'three'})"
s2 = "( var x = 10; y: (1, 2, 3] } )"

st = Stack()
if st.check(s1):
	print ("Right syntax")
else:
	print ("Wrong sytnax")
print (s1)

if st.check(s2):
	print ("Right syntax")
else:
	print ("Wrong sytnax")
print (s2)

