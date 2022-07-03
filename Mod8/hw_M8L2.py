import sqlite3
#import json
from pprint import pprint

print(' hello from module 8 level 2 homework ! ')

student_list = [(1, 'Max', 'Brooks', 24, 'SPb'),
(2, 'John', 'Stones', 15, 'SPb'),
(3, 'Andy', 'Wings', 45, 'Manchester'), 
(4, 'Kate', 'Brooks', 34, 'SPb')]

print('\n student_list :')
pprint(student_list)

course_list = [(1, 'python', '21.07.21', '21.08.21'),
(2, 'java', '13.07.21', '16.08.21')]

print('\n course_list :')
pprint(course_list)

studying_list = [(1, 1), (2, 1), (3, 1), (4, 2)]

#print('\n student_list : \n', student_list)
#print('\n course_list : \n', course_list)
print('\n studying_list : \n', studying_list)

conn = sqlite3.connect('db_university2.sqlite')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))')
# s = 'CREATE TABLE Cources (id int, subject Varchar(64), time_start Varchar(10), time_end Varchar(10))'
# cursor.execute(s)
# s = 'CREATE TABLE Studies (id_student int, id_course int)'
# cursor.execute(s)


# cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', student_list)
# cursor.execute('SELECT * FROM Students')
# print('\n selected from database - table Students : \n', cursor.fetchall())

# cursor.executemany('INSERT INTO Cources VALUES (?, ?, ?, ?)', course_list)
# cursor.execute('SELECT * FROM Cources')
# print('\n selected from database - table Cources : \n', cursor.fetchall())

# cursor.executemany('INSERT INTO Studies VALUES (?, ?)', studying_list)
# cursor.execute('SELECT * FROM Studies')
# print('\n selected from database - table Studies : \n', cursor.fetchall())

cursor.execute('''SELECT name, surname, age FROM Students WHERE age > 30 ''')
print('\n request from database - Students > 30: \n', cursor.fetchall())

cursor.execute('''SELECT id_student, id_course FROM Studies WHERE id_course == 1 ''')
request_list = cursor.fetchall()

#a = []
print('''\n python's students : ''')
for t in request_list:
	nm = t[0]
	cursor.execute(f'SELECT name, surname, city FROM Students WHERE id == {nm};')
	s = cursor.fetchall()
#	a.append(s)
	if s != [] : print(s)

#print(' a : ', a)	

print('''\n python's students in SPb: ''')
for t in request_list:
	nm = t[0]
	cursor.execute(f'''SELECT name, surname, city FROM Students WHERE id == {nm} AND city == 'SPb';''')
	s = cursor.fetchall()
	if s != [] : print(s)

#print(cursor.fetchall())

conn.commit()
conn.close()