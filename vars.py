# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 14:40:49 2022

@author: prubac
"""

a = 36674373475217527592715924759875987125902175907598217590215792157829017
b = 36674373475217527592715924759875987125902175907598217590215792157829017.36
#b = 0.00000000000000000000003525
print(type(a))
print(type(b))
print(a)
print(b)

c = a + 1
print(c)
d = b + 1
print(d)

v = 0b101
print(v)
h = 0x11
print(h)

s1 = '2142'
print(int(s1))
print('c=' + str(c))
print(f'c={c}')
print('c={}'.format(c))

s2 = 'sagsagjkakgsgsnj'
print(s2[2:6])
print(s2[2:])
print(s2[:2])
print(s2[-2:])
print(len(s2))

s3 = 's\'ags\\nagjka\tkgsgsnj'
print(s3)

s4 = "s'ags\\nagjka\tkgsgsnj"
