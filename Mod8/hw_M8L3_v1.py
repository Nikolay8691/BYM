import sqlite3
from pprint import pprint
from peewee import *

print(' hello from module 8 level 3 homework ! ')

student_list = [(1, 'Max', 'Brooks', 24, 'SPb'),
(2, 'John', 'Stones', 15, 'SPb'),
(3, 'Andy', 'Wings', 45, 'Manchester'), 
(4, 'Kate', 'Brooks', 34, 'SPb')]

print('\n student_list :')
pprint(student_list)

rows_students = []
for person in student_list:
	student = {}
	student['st_id'] = person[0]
	student['name'] = person[1]
	student['surname'] = person[2]
	student['age'] = person[3]
	student['city'] = person[4]
	rows_students.append(student)
# print(' rows_students : \n', rows_students)

course_list = [(1, 'python', '21.07.21', '21.08.21'),
(2, 'java', '13.07.21', '16.08.21')]

print('\n course_list :')
pprint(course_list)

rows_courses = []
for subject in course_list:
	course = {}
	course['co_id'] = subject[0]
	course['title'] = subject[1]
	course['time_start'] = subject[2]
	course['time_end'] = subject[3]
	rows_courses.append(course)
# print(' rows_courses : \n', rows_courses)

studying_list = [(1, 1), (2, 1), (3, 1), (4, 2)]
print('\n studying_list : \n', studying_list)

rows_studies = []
for s_edu in studying_list:
	study = {}
	study['id_student'] = s_edu[0]
	study['id_course'] = s_edu[1]
	rows_studies.append(study)
# print(' rows_studies : \n', rows_studies)

db = SqliteDatabase('db_university3_v1.sqlite')

class Students(Model) :
	st_id = IntegerField()
	name = TextField()
	surname = TextField()
	age = IntegerField()
	city = TextField()

	class Meta:
		database = db 
		db_table = 'Students'

class Courses(Model) :
	co_id = IntegerField()
	title = TextField()
	time_start = TextField()
	time_end = TextField()

	class Meta:
		database = db
		db_table = 'Courses'

class Studies(Model) :
	id_student = IntegerField()
	id_course = IntegerField()

	class Meta:
		database = db
		db_table = 'Studies'


# db.create_tables([Students])
# q = Students.insert_many(rows_students)
# q.execute()	

# db.create_tables([Courses])
# q = Courses.insert_many(rows_courses)
# q.execute()


# db.create_tables([Studies])
# q = Studies.insert_many(rows_studies)
# q.execute()
# qry = Studies.delete()
# qry.execute()

rows = Students.select()
print('\nDatabase table_data - Students full list : ')
for buddy in rows :
 	print(buddy.name, buddy.age, buddy.city)

rows = Courses.select()
print('\nDatabase table_data -  Courses full list : ')
for subj in rows :
 	print(subj.co_id, subj.title) 

rows = Studies.select()
print('\nDatabase table_data -  Studies full list : ')
for s_edu in rows :
 	print(s_edu.id_student, s_edu.id_course)

# # s1 = Students(st_id = 3, name = 'Andy', surname = 'Wings', age = 45, city = 'Manchester')
# # s1.save()

# # buddy = student_list[3]
# # c1 = buddy[0]
# # c2 = buddy[1]
# # c3 = buddy[2]
# # c4 = buddy[3]
# # c5 = buddy[4]
# # print(' c1-5 : ', c1, c2, c3, c4, c5)
# # print(f'st_id = {c1}, name = {c2}, surname = {c3}, age = {c4}, city = {c5}')
# # print('st_id = %d, name = %s, surname = %s, age = %d, city = %s' %(c1,c2,c3,c4,c5))
# # s1 = Students(f'st_id = {c1}, name = {c2}, surname = {c3}, age = {c4}, city = {c5}')
# # s1 = Students('st_id = %d, name = %s, surname = %s, age = %d, city = %s' %(c1,c2,c3,c4,c5))
# # s1.save()

rows = Students.select().where(Students.age > 30) 
#print(rows.sql())
print('\n short list Students > 30 : ')
for buddy in rows :
 	print(buddy.name, buddy.age, buddy.city)

subject_f = 'python'
co_id_f = -1
for subj_f in course_list :
	if subj_f[1] == subject_f : co_id_f = subj_f[0]
# print(f'''\n {subject_f}'s course_id = {co_id_f} : ''')

if co_id_f != -1 :
	# print(f'''\n short list {subject_f}'s Students : ''')
	# rows = Studies.select()
	rows = Studies.select().where(Studies.id_course == co_id_f)
	subject_f_student = []
	for s_edu in rows :
		s = s_edu.id_student		
		subject_f_student.append(s)
		# print(s_edu.id_student, s_edu.id_course)

	print(f'''\n short list {subject_f}'s Students : \n''')
	for student_course in subject_f_student:
		rows = Students.select().where(Students.st_id == student_course)		
		for buddy in rows :
 			print(buddy.name, buddy.age, buddy.city)

	print(f'''\n short list {subject_f}'s Students in SPb: \n''')
	for student_course in subject_f_student:
		rows = Students.select().where((Students.st_id == student_course) & (Students.city == 'SPb'))		
		for buddy in rows :
 			print(buddy.name, buddy.age, buddy.city) 	

else:
	print(f'''\nnobody studies {subject_f}'s progs''')

db.close()