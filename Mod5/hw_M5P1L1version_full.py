import json

class StringVar():
	s = 'start again ! '

#	def __init__(self, s1):
#		if type(s1) == str : 
#			print(' good start, this variable is string ! ')
#			self.s = s1
#		else:
#			print(' this variable is supposed to be of type string. try it again ')
#			self.s = ' 42 '

	def fprint(self):
		print(' ', self.s)
		pass

	def set(self, s1):
		if type(s1) == str : 
			print(' good start, this variable is string ! ')
			self.s = s1
		else:
			print(' this variable is supposed to be of type string. try it again ')
#			self.s = ' 42 '
		pass

	def get(self):
		return self.s

# main program
print(' hello it is Module 5 Part 1 level 1 exercise ! ')


a = StringVar()

#word = input(' type something looking similar to a string : ')
#word2 = 'football'				#1
#word2 = 42						#2
#word2 = [9, 1, 3]				#3
#word2 = (7, 3 ,6)				#4
#word2 = {9, ' flist '}			#5
word2 = {"startlogin": "brunoym123", "nikolay": "sport123", "alla": "nosport123"}

#word2 = [[9, 70, 20, 67, 33], 	#6
#    [60, 20, 94, 14,77],
#    [27, 58, 45, 0, 13],
#    [39, 47, 25, 97,69],
#    [83, 13, 100, 1, 85]]

#if word == '42' : word2 = 42
#else: word2 = word

with open('data511_type5.json', 'w') as f:
	json.dump(word2, f)

with open('data511_type5.json', 'r') as f:
	word1 = json.load(f)

#a = StringVar(word1)
a.set(word1)

#a.fprint()
print(' print as an attribute of StrinVar class (not via methods) : ', a.s)

s = a.get()
print(' string from class StringVar (via get - method) = ', s)