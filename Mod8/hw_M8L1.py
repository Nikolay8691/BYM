import sqlite3

print(' hello from module 8 level 1 homework ! ')

conn = sqlite3.connect('db_university.sqlite')

cursor = conn.cursor()

#cursor.execute('CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))')
# s = 'CREATE TABLE Cources (id int, subject Varchar(64), time_start Varchar(10), time_end Varchar(10))'
# cursor.execute(s)
#cursor.execute('CREATE TABLE Students (id int, name Varchar(32), surname Varchar(32), age int, city Varchar(32))')

student_list = [(1, 'Ilya', 'Petrov', 19, 'SPb'),
(2, 'Maxim', 'Ivanov', 20, 'Msc'), 
(3, 'Fedor', 'Petrov', 21, 'SPb')]

course_list = [(1, 'Math', '2022-01-11', '2022-05-31'),
(2, 'IT', '2022-04-02', '2022-05-30'), 
(3, 'Chinese-2 for_beginners', '2022-01-13', '2022-03-31')]

print('\n student_list : \n', student_list)
print('\n course_list : \n', course_list)

cursor.executemany('INSERT INTO Students VALUES (?, ?, ?, ?, ?)', student_list)
cursor.execute('SELECT * FROM Students')
print('\n selected from database - table Students : \n', cursor.fetchall())


cursor.executemany('INSERT INTO Cources VALUES (?, ?, ?, ?)', course_list)
cursor.execute('SELECT * FROM Cources')
print('\n selected from database - table Cources : \n', cursor.fetchall())

# print(' student : ', 'id, name, surname, age, city ')
# print(' courses : ', 'id, subject, time_start, time_end ')
# print(' student_course : ', 'student_id, course_id ')
conn.commit()
conn.close()