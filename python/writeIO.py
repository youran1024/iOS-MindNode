

f = open('/Users/MrYang/Desktop/python/1.py', 'r')

print(f.read())

try:
	f = open('/Users/MrYang/Desktop/python/1.py', 'r')
	print(f.read())
finally:
	if f:
		f.close()	
	

