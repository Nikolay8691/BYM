import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(''' flud's name = ''', thread_name)

#main prog

print(' welcome to module {} level {} -- fluds and process progs'.format(6,1))

rivers = ['amazonas', 'missisipi', 'نيل', 'волга', '黄河']

threads = [Thread(target = get_thread, args = (s, )) for s in rivers]

for t in threads:
	t.start()

for t in threads:
	t.join()
