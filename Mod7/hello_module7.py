print(' hello! It is module 7, tervetuloa! ')
s = input(' what is your name? ')
day_period = ' morning ' 
print(f' good {day_period} nice to see you, {s} : f-string \n ')

print(' good %s nice to see you, %s: old_format \n ' %('morning',s))

print(' good {} nice to see you, {} : format-func '.format(day_period,s))