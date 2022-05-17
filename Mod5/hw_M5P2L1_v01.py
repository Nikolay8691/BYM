import json
from pprint import pprint

class Model() :
	def __init__(self, x, y, title, script, author, time_date, jfile, obj_name):
		self.x = x
		self.y = y
		self.title = title
		self.script = script
		self.author = author
		self.time_date = time_date
		self.jfile = jfile

#		print(' __init__ just before save_method !')

		self.id = 0
		self.save()

	def set(self, x, y, title, script, author, time_date, jfile, obj_name):
		self.x = x
		self.y = y
		self.title = title
		self.script = script
		self.author = author
		self.time_date = time_date
		self.jfile = jfile

		self.save()

	def save(self):
		str_id = obj_name + '_' + str(self.id)
		newrec = self.__dict__
		dict_newrec = {str_id : newrec}
		#dict_newrec = {str(self.id) : {'x' : self.x, 'y' : self.y, 'script' : self.script, 'author' : self.author, 'time_date' : self.time_date}}
		#dict_newrec = {str(self.id) :[self.x, self.y, self.title, self.script, self.author, self.time_date]}

		print(' id = ', str_id, 'new record : ')
		pprint(newrec)
#		print(' save_method dict_newrec is on, start json file ! ')
#		model_data = self.jfile
		
#		if self.id == 0 :
#			with open(model_data, 'w') as f:
#				json.dump(dict_newrec, f)
#		else:
#			with open(model_data, 'a') as f:
#				json.dump(dict_newrec, f)

		with open('model_data.json', self.jfile) as f:
				json.dump(dict_newrec, f)
		
		self.id += 1

#main program

print('')
print('')

#l = []

x = 5
y = 6
title = 'zero-point'
script = ' this is the coldest point in the world ! '
author = ' Andersen '
time_date = 1900
#jfile = 'model_data1.json'
jfile = 'w'
obj_name = 'poles1'

p1 = Model(x, y, title, script, author, time_date, jfile, obj_name)

print('')
print('')

x = 0
y = 0
title = 'South Pole'
script = ' it is very far on the south but it is also one of the coldest points in the world ! '
author = ' Magellan '
time_date = 1789
#jfile = 'model_data1.json'
jfile = 'a'
obj_name = 'poles1'

p1.set(x, y, title, script, author, time_date, jfile, obj_name)

print('')
print('')

x = 1
y = 2
title = 'zero-point2'
script = ' this is the coldest point in the world ! '
author = ' Andersen2 '
time_date = 1902
#jfile = 'model_data2.json'
jfile = 'a'
obj_name = 'poles2'

p2 = Model(x, y, title, script, author, time_date, jfile, obj_name)

print('')
print('')

x = 2
y = 3
title = 'South Pole2'
script = ' it is very far on the south but it is also one of the coldest points in the world ! '
author = ' Magellan2 '
time_date = 1702
#jfile = 'model_data2.json'
jfile = 'a'
obj_name = 'poles2'

p2.set(x, y, title, script, author, time_date, jfile, obj_name)

print('')
print('')
