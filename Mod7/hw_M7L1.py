import requests
from bs4 import BeautifulSoup
import json

#from pprint import pprint

import ctypes

kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# ANSI colors
c = (
    "\033[0m",   # End of color
    "\033[36m",  # Cyan
    "\033[91m",  # Red
    "\033[35m",  # Magenta
)

print(c[1] + '\n hello! It is module 7 level 1, tervetuloa hyvät ystävät! \n'+ c[0])

link = ('USD', 'https://mfd.ru/currency/?currency=USD')
count = 0
web_p = requests.get(link[1])
req_code = web_p.status_code

if 200 <= req_code < 300 :

	soup = BeautifulSoup(web_p.text, 'html.parser')
	#print(type(soup))
	
	rates = soup.find_all('table', class_='mfd-table mfd-currency-table') #rates = soup.find_all('table', {'class' : 'mfd-table mfd-currency-table'})
	for rate in rates:
		if count >= 10 : 
			print(c[2] + ' count = ', count, 'process is stopped !' + c[0])
			break
		else:
			count += 1
			
#			print([rate.text] , '\n rate_text type is : ' , type(rate))
			print(' count = ', count)
			
	print('\n', link, ' web page is in work ')

	with open((link[0] + '_rates.json'), 'w') as f:
		json.dump(rate.text, f)

else:
	print(c[2] + ' something went wrong while pinging ', link)
	print(' code of return = ', req_code, ' ! ' + c[0])

s = ''
with open((link[0] + '_rates.json'), 'r') as f:
	s = json.load(f)

print('\n s-string_from_json : ', s[-30:-19])

# l = s[-30:-28]
# key_combi = l

key_combi = 'с '
# print(' key_combi =', [key_combi], ' s[-30] : ', [s[-30]], ' s[-29] : ', [s[-29]],
#  ' s[-30:-28] : ', [s[-30:-28]])

imax = len(s)
j = 0
date_rate = []
ex_rate = []

for i in range(imax):
#	if j == 10 : break
	if s[-(i+2):-(i)] == key_combi:	
		date_rate.append(s[(imax - i) : (imax - i + 10)])
		ex_rate.append(s[(imax - i + 11) : (imax - i + 18)])
		j += 1
		
jmax = j
print(' jmax = ', jmax, '\n')
date_and_rate = []

for j in range(jmax):
	print(' date : ' , date_rate[j] , ' rate = ', ex_rate[j])
	date_and_rate.append([date_rate[j], ex_rate[j]])

with open(('date_and_rates.json'), 'w') as f:
	json.dump(date_and_rate, f)

