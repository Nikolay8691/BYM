import requests
import time
import json
from threading import Thread
#import pprint

def get_html(link):

	web_p = requests.get(link[0])
	req_code = web_p.status_code

	if 200 <= req_code < 300 :

#		print(link, 'web headers : \n', web_p.headers)
		print(link, 'web page is in work ')
		with open((link[1] + '_text.json'), 'w') as f:
			json.dump(web_p.text, f)

#		print(link, 'web text : \n', web_p.text)
	else:
		print(' something went wrong while pinging ', link)
		print(' code of return = ', req_code)

#main program
print(' hello from module 6 and requests - exercise 3 \n')
start_time = time.time()

# s = ('https://spb.arbitr.ru', 'SPb A_court')
# get_html(s)

# s = ('https://www.pochta.ru/tracking', 'pochta')
# get_html(s)

s5 = [('https://www.pochta.ru/tracking', 'pochta'),
('https://promneokom-spb.ru/', 'promneokom-spb'),
('https://yandex.ru/', 'YANDEX'),
('https://www.youtube.com/', 'YOUTUBE'),
('https://rp5.ru/', 'Weather')]

print('calculations with usual processes started : \n')

for s in s5:
	get_html(s)

end_time_1 = time.time() - start_time
print('--- %s seconds    ' % round(end_time_1,3))
x1 = (end_time_1, 'usual')

print(' calculations with usual processes finished :')
print('\n calculations with parallel processes started : \n')

threads = [Thread(target = get_html, args = (s, )) for s in s5]

for t in threads:
	t.start()

for t in threads:
	t.join()

end_time_2 = time.time() - (start_time + end_time_1)
print('--- %s seconds    ' % round(end_time_2,3))
#end_time_2 = datetime.now()
x2 = (end_time_2, 'parallel')

print(' calculations with parallel processes finished :')
print(f'\n duration with usual process = {x1[0]} ')
print(f' duration with parallel process = {x2[0]} ')

max1 = (x1[0] >= x2[0]) * x1 + (x2[0] > x1[0]) * x2
print('\n Maximum of these two is = ', max1)

#r = requests.get('https://github.com/timeline.json', headers = headers)

#print('\n all processes are finished ')
