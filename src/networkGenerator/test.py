'''
Created on 2017/04/16

@author: smallcat
'''

a = {}
if (3,2) not in a:
    a[(3,2)] = 4
print a
if (3,2) in a:
    a[(3,2)] = a[(3,2)] + 1
print a

b = [5,6,8]
print b[2]
#print b(2)

c = (3,4)
print c[0]

d = [3,4]
d.remove(4)
d.append(5)
print d

import copy
e = [3,4]
f = copy.copy(e)
print f
f.append(5)
print e
print f

for g in range(2,4):
    print g
    
h = {3:8, 9:2, 6:5}
print h[3]
print h.keys()

h = sorted(h.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)
print h
print h[0][1]

i = {2:3, 4:6, 9:5}
i.pop(4)
print i

j = [((3,8),6), ((9,2),5), ((6,5),7)]
print j[0][0][0]

k = (4,7)
if 4 in k:
    print "yes"
for i in iter(k):
    print i
for i in k:
    print i

pair_dis = [((3,8),6), ((9,2),5), ((6,5),7), ((2,8),4), ((9,3),5)]    
for i in pair_dis:
    if 2 in i[0]:
        pair_dis.remove(i)
print pair_dis

routes = {3:5, 6:8}
for r in routes.items():
    print r[1]
if 4 in routes.keys() and routes[4] > 1:
    print "yes"
    
x = [4,5,6,7,8,9]
print x[-2]
x.pop(0)
x.pop(-1)
print x

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]
print [l for l in list1 if l in list2]

routes.pop(6)
print routes

b = 4
a = b
b = 5
print a

x = []
def change(x):
    x = changex(x)
def changex(x):
    x.append(1)
    return x
change(x)
print x

yy = 0
y = {1:[2], 3:[6,8]}
for item in y.values():
    yy = yy + len(item)
print yy
if 1 in y:
    print " yes "
if 4 in y:
    print " no "
    
for i in range(4, 7):
    print i
    
i = [3, 5]
k = [4, 5]
j = [2,3,5,6]
if i in j:
    print "yes i"
if k in j:
    print "yes k"
    
k = {2:[4,5]}
k[2].remove(4)
print k

j = [4,5,6]
for i in j:
    j = [7,8,9]
    print i