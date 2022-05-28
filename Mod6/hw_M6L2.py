import time
from threading import Thread
from datetime import datetime

def get_thread(thread_name):
	time.sleep(1)
	print(''' flud's name = ''', thread_name)

#main prog
start_time = datetime.now()
#start_time = time.time()

print(' welcome to module {} level {} -- fluds and process progs'.format(6,2))

rivers = ['amazonas', 'missisipi', 'نيل', 'волга', '黄河']


print('\n calculations with parallel processes started :')
threads = [Thread(target = get_thread, args = (s, )) for s in rivers]

for t in threads:
	t.start()

for t in threads:
	t.join()

#print('--- %s seconds    ' % (time.time() - start_time))
end_time_1 = datetime.now()
x1 = (end_time_1 - start_time, 'parallel')

print(' calculations with parallel processes finished :')
print('\n calculations with usual processes started :')

for s in rivers:
	get_thread(s)

end_time_2 = datetime.now()
x2 = (end_time_2 - end_time_1, 'usual')
print(' calculations with usual processes finished :')
print(f'\n duration with parallel process = {x1[0]} hours : minutes : seconds')
print(f' duration with usual process = {x2[0]} hours : minutes : seconds')

max1 = (x1[0] >= x2[0]) * x1 + (x2[0] > x1[0]) * x2
print('\n Maximum of these two is = ', max1[1])


