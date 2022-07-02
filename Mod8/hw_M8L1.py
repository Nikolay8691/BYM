import sqlite3
import json
from pprint import pprint

print(' hello from module 8 level 1 homework ! ')



# student_list = [(1, 'Ilya', 'Petrov', 19, 'SPb'),
# (2, 'Maxim', 'Ivanov', 20, 'Msc'), 
# (3, 'Fedor', 'Petrov', 21, 'SPb')]

# with open(('students.json'), 'w') as f:
# 	json.dump(student_list, f)

with open(('students.json'), 'r') as f:
	student_list = json.load(f)	

print('\n student_list :')
pprint(student_list)

course_list = [(1, 'Math', '2022-01-11', '2022-05-31'),
(2, 'IT', '2022-04-02', '2022-05-30'), 
(3, 'Chinese-2 for_beginners', '2022-01-13', '2022-03-31')]

print('\n course_list :')
pprint(course_list)

studying_list = [(1, 2), (1, 3), (2, 2), (3, 1), (3, 2)]

#print('\n student_list : \n', student_list)
#print('\n course_list : \n', course_list)
print('\n studying_list : \n', studying_list)

conn = sqlite3.connect('db_university.sqlite')

cursor = conn.cursor()

#cursor.execute('CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))')
# s = 'CREATE TABLE Cources (id int, subject Varchar(64), time_start Varchar(10), time_end Varchar(10))'

# s = 'CREATE TABLE Studies (id_student int, id_course int)'
# cursor.execute(s)


#cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', student_list)
cursor.execute('SELECT * FROM Students')
print('\n selected from database - table Students : \n', cursor.fetchall())


#cursor.executemany('INSERT INTO Cources VALUES (?, ?, ?, ?)', course_list)
cursor.execute('SELECT * FROM Cources')
print('\n selected from database - table Cources : \n', cursor.fetchall())

#cursor.executemany('INSERT INTO Studies VALUES (?, ?)', studying_list)
cursor.execute('SELECT * FROM Studies')
print('\n selected from database - table Studies : \n', cursor.fetchall())

conn.commit()
conn.close()