
import math

a = 100
if a < 10:
	print(a)
else:
	print(-a)

string = '123'

print(string)

print('Hi, %s, you have a $%d' % ('Micles', 10000))


string = 'Hi, %s, you have $%d' % ('Jack', 102000)

print(string)


s1 = 72
s2 = 85

r = s1 / 100 - s2 / 100

print('xiaoming rive %.2f' % abs(r))

users = ['Micle', 'Jack', 'Bob']

print(users)

print(len(users))

print(users[1])

print(users.append('Adma'))

users.append('sdf')

print(users)

users.insert(1, '1111')

print(users.insert(1, 'fffff'))

l = ['Apple', 123, True]

print(l)

s = ['Asp', 'java', ['asp1', 'php'], 'scheme']

print(s)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0], L[1][1], L[2][2])

print('========================================')

for name in L:
	for string in name:
		print(string)


print(list(range(5)))

for x in list(range(10)):
	print(x)

L = ['Bart', 'Lisa', 'Adam']

print('======================================')

for name in L:
	print('Hello:%s'% name)

print('======================================')

for name in L:
	print('Hello:' + name)

print('======================================')

for name in L:
	print('Hello:',name)


dict = {'name': 'jace', "sex": "male", 'age': 19}

print(dict)

#	判断Key是不是在字典里变

# Method1
print('name' in dict)

print('jace' in dict)

# Method2 (可定制返回数据， 默认是None)
print(dict.get('Thomas'))

print(dict.get('Thomas', 'bucunzai'))

# 字典里边删除数据 (key是必须存在的)
dict.pop('name')

print(dict)

# set 不允许重复数值，对于重复数值自动过滤
s = set([1, 7, 3, 3, 5])

print(s)

sl = ['a', 'z', 'v']

sl.sort()

print(sl)


j1 = [1, 3, 2, 9, 6]

j1.sort()

print(j1)

def sumabc(a, b, c):

	if not isinstance(a, (int, float)):
		raise TypeError('bad operand type')

	return a + b + c


sumabc(1, 3, 5)

def  move(x, y, step, anle = 0):
	nx = x + step * math.sin(anle)
	ny = y + step * math.cos(anle)

	return nx, ny

x, y = move(1, 2, 3, math.pi / 6)

print('%.2fand%.2f' % (x, y))


# /////////////////////////////////////////
#
#             函数
#
#/////////////////////////////////////////

from math import sqrt
def same(x,*fs):
    [f(x) for f in fs]
    return s

print(same(4,sqrt,abs))

abs = 10

# 用del 恢复abs的使用
del abs 

print(abs(-5))


def power(x, n = 2):

	r = 1
	while n > 0:
		n -= 1
		r *= x

	return r

print(power(5, 2))

print(power(5))

def add_start(l):
	if not isinstance(l, list):
		raise('pass error')
	l.append('start')

	return l


print(add_start([5, 6]))

print(add_start([]))


def  add_end(l=[]):
	return

array = []
array.append(1)

print(array)

array.append(1)

print(array)

print([])


def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n

	return sum

calc(12, 2, 5)

print(calc(1, 2, 3))

print(calc())


numbers = [1, 2, 3, 4, 5, 6]

print(numbers[1:2])

for i in range(3):
	print(i)

print('===========================================')

for i in range(3,10):
	print(i)


import os
array = [d for d in os.listdir('.')]
print(array)

a, b, c = 1, 2, 3

print(a, b, c)

def triangles():
	array = []
	for  i in range(0, 11):
		arrayTmp = []
		for j in range(0, i):
			if (j == 0 ):
				arrayTmp.append(1)
			elif (j == i - 1):
				arrayTmp.append(1)
			else:
				arrayJ = array[i - 1]
				arrayTmp.append(arrayJ[j] + arrayJ[j - 1])
				

		yield arrayTmp		
		array.append(arrayTmp)


	return array

for x in triangles():
	print(x)

def triangles1():
	arrayTmp = [1]
	array.append(arrayTmp)
	for i in range(0,10):
		arrayTmp = []

print('========================================')

def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

print('==========================================')

array = [1, 2, 3, 4]
array1 = [1, 2, 3, 4]
print(array + array1)


def trigles2():
	li = [1]
	while True:
		yield li
		li = [1] + [sum(a) for a in zip(li[:-1], li[1:])] + [1]


n = 0
for x in trigles2():
	print(x)
	n += 1
	if n == 10:
		break


def trigles3():
	li = [1]
	while True:
		yield li
		li = [1] + [sum(a) for a in zip(li[1:], li[:-1])] + [1]


print('*******************************************')

n = 0
for x in trigles3():
	print(x)
	n += 1
	if n == 10:
		break

print('----------------------------------------------')



def sumx(x):
	return {'1' : 1 , '2' : 2 , '3' : 3 }[x]

print(map(sumx, '123'))

for x in map(sumx, '123'):
	print(x)

#x = input()
x = 'FKLD'
def stringFormat(x1):
	return x1.lower()

y = map(stringFormat, x)
s = ''
for string in y:
	s += string

print(s)


def nameFormat(x):
	return x[0].upper() + x[1:].lower()

for x in map(nameFormat, ['SfDF', 'SLFWF', 'sdfSS']):
	print(x)

def count():
	l = []
	for i in range(1,  4):
		def  g():
			return i * i

		l.append(g())
	return l

print(count(), count(), count())

f1 = count()
f2 = count()
f3 = count()

print(f1, f2, f3)

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1, f2, f3)

print('123')
print(int('123', base = 8))

def  int2(x):
	return int(x, base = 8)

def  int2(x, base = 2):
	return int(x, base)

import functools

int2 = functools.partial(int, base = 2)

print(int2('1000'))
kw = {'base' : 2}

print(int('1000', **kw))


from PIL import Image
try:
	im = Image.open('1.png')

	print(im, im.size, im.mode, im.format)
	im.thumbnail((100, 200))
	im.save('hello.png', 'PNG')

except:
	pass

finally:

	pass

class  student(object):
	"""docstring for  student"""
	def __init__(self, arg):
		super( student, self).__init__()
		self.arg = arg

	@property
	def score(self):
		return self._score

import pdb

#pdb.set_trace()

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


from io import StringIO

f = StringIO()
f.write('hello,\n world \n good')
f.seek(0)

while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())

import os
print(os.name)

print(os.uname)

import pickle

d = {'name':'Bob', 'age':20, 'score':88}
pickle.dumps(d)

f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()

print('--------------------------------')

f = open('dump.txt', 'rb')
d = pickle.load(f)
f.close
print(d)

import json

f = open('dump.txt', 'wb')
json.dumps(d, f)
f.close


print('------------------------------------------')
print('多进程')

import os

print('Process (%s) start...' % os.getpid())
#pid = os.fork()
pid = 0

if pid == 0:
	print('sub process (%s) and parent is %s' %(os.getpid(), os.getpid()))
else:
	print('parent process (%s) create sub process %s' % (os.getpid(), pid) )

import threading, multiprocessing

def loop():
	x = 0
	while True:
		print('gogogo')
		x = x ^ 1


#for i in range(multiprocessing.cpu_count()):
#	pass
	#t = threading.Thread(target = loop)
	#break

print('--------------------------------------------')
print('	正则表达式')
print('--------------------------------------------')

import re

str = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
print(str)

str = re.match(r'\d{3}[\-, ,\s]?\d{3,8}$', '113	12345')
print(str)

str = re.split(r'[\s\,]', 'a, b, cd')
print(str)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m)

re_mail = re.compile(r'^[\w]{1}[\w\d]+.?[\w\d]*@[\w|\d]+.[\w]+$')

m = re_mail.match('a1.@163.com')
print(m)

print(re_mail.match('someone@gmail.cn'))

print(re_mail.match('bill.gate@Microsoft.com'))

print('----------------------------------')
print('dateTime')

from datetime import datetime

print(datetime.now())

print(datetime.now().timestamp())


import base64

def safe_base64_decode(s):
	c = len(s)*6%48 * 48 - len(s)
	s = s + '='* int(len(s) % 4)
	s = base64.b64decode(s)
	return s

s = safe_base64_decode('YWJjZA')
print(s)

import hashlib

md5 = hashlib.md5()
md5.update('how to user md5 in'.encode('utf-8'))
md5.update('python hashlib?'.encode('utf-8'))
print(md5.hexdigest())


import itertools

natuals = itertools.count(2)
print(natuals)

for n in natuals:
	print(n)
	if n == 3:
		break

cs = itertools.cycle('AVC')

i = 0
for c in cs:
	print(c)
	if i == 3:
		break
	i += 1

ns = itertools.repeat('ABC', 3)

print(list(ns))

for c in ns:
	print(c)

natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)

print(list(ns))

for n in ns:
	print(n)


naturals = itertools.repeat('AFBV')


for c in itertools.chain('ABC', 'CVF'):
	print(c)


for key, group in itertools.groupby('sdf12112233aaff'):
	print(key, list(group))

for key, group in itertools.groupby('aaAAsdsSSDdd', lambda x: x.upper()):
	
	print(key, list(group))





