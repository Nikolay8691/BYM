import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
from pprint import pprint

l = []
with open('date_and_rates.json', 'r') as f:
	l = json.load(f)	

#pprint(l)

date = []
rate = []

for one in l:
	date.append(one[0])
	rate.append(float(one[1]))

s = ' exchange rates from ' + date[0] + ' up to ' + date[-1]
print(s, type(s))

months = mdates.MonthLocator()
days = mdates.DayLocator()

fig, ax = plt.subplots()
plt.plot(date, rate, color = 'red', label = 'USD')
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(days)
ax.set_title(s)
ax.set_ylabel(' e-rate, rbl ')
ax.grid(True)
ax.legend(loc = 'upper left', frameon = False)

plt.show()