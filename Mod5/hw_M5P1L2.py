print(' hello! it is Module 5 part 1 level 2 homework exercise. ')

class Point():

	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def distance(self):
		return (self.x**2 + self.y**2)**(1/2)

	def __add__(self, other):
		return Point(self.x + other.x, self.y + other.y)

	def set(self, x, y):
		self.x = x
		self.y = y

	def get(self):
		return Point(self.x, self.y)

# main program

#p0 = (x0, y0)
#p1 = Point(p0[0], p0[1])

p1 = Point(0, 0)
p2 = Point(0, 0)
it = 0

# while True and it < 10 :
while True :
	
	delta_x = 0 
	delta_y = 0
	it += 1

	print(' what are you going to do ? ')
	print(' 1 - set new point ')
	print(' 2 - move right / left / up / down ')
	print(' 3 - find distance to zero-point / between two points ')
	print(' 4 - get current point coordinates ')
	print(' 5 - stop program ')
	sw = int(input(' '))

	if sw == 5 : break
	elif sw == 1 : #1 set point
		x = int(input(' input coordinate x of the point '))
		y = int(input(' input coordinate y of the point '))
		p2 = Point(x ,y)
		print(' new point is created. Coordinates : x = ', p2.x, ' y = ', p2.y)

	elif sw == 2 : #2 move right / left +-x (+- other.x) | up / down  +-y (+- other.y)
		print(' horizontal move (along x-axis) left / right / no ? ')
		x_move = input()
		if x_move == 'left' : 
			delta_x = -int(input(' to how many points move to the left ? '))
		elif x_move == 'right' : 
			delta_x = int(input(' to how many points move to the right ? '))
		else :
			delta_x = 0
			print(' Ok, no move in horizontal direction ')

		print(' vertical move (along y-axis) up / down / no ? ')
		y_move = input()
		if y_move == 'down' : 
			delta_y = -int(input(' to how many points move down ? '))
		elif y_move == 'up' : 
			delta_y = int(input(' to how many points move up ? '))
		else :
			delta_y = 0
			print(' Ok, no move in horizontal direction ')
		p2 = p1 + Point(delta_x, delta_y)
		print(' new point coordinates are : x = ', p2.x, ' y = ', p2.y)
		print(' old point coordinates are : x = ', p1.x, ' y = ', p1.y)

	elif sw == 3 : #3 find distance from zero-point / find distance between 2 points
		print(' 1 - to find distance from zero-point ')
		print(' 2 - to find distance between 2 point (new and previous) ')
		sw2 = int(input())
		if sw2 == 1 : 
			x = int(input(' input coordinate x of the point '))
			y = int(input(' input coordinate y of the point '))
			p2 = Point(x ,y)
#			dist = p2.distance()
			print(' distance from zero-point is ', round(p2.distance(),2), ' cm ')
		elif sw2 == 2 :
			x = int(input(' input coordinate x of new point '))
			y = int(input(' input coordinate y of new point '))
			p2 = Point(-x ,-y)
			p3 = p1 + p2
#			dist = p3.distance()
			print(' distance between new and old points is ', round(p3.distance(),2), ' cm ')
		else:
			print(' wrong switch key ! ')


	elif sw == 4 : #8 get current coordinates
		p2 = p1.get()
		print(' current point coordinates are : x = ', p2.x, ' y = ', p2.y)

	else: 
		print(' wrong switch key ! ')

	p1 = p2
	print()
	print()

