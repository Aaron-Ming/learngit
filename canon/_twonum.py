#!/usr/bin/env python
#encoding=utf8
#
'''
定义一个列表，然后定义一个值resule，从列表中查找任意两个相加等于result的值。
首先定义一个空字典，将每个列表中的值被result减，得出的值作为字典的key，对应的索引值作为key的value
那么然后，进行判断
'''

arr = [1,2,3,10,7,9,22,30,33,12]
need_dict = {}
result = 31

length = len(arr)
print "本次要求相加等于%d" % (result)
for i in range(length):
    num = arr[i]
    need = result - num
    if num in need_dict:
#        print need
#        print "The %d index %d" % (num, i)
#        print "The %d index %d" % (arr[need_dict[num]], need_dict[num])
#        print "本次要求相加等于%d" % (result)
        print "Num %d index %d and num %d index %d" % (num, i, arr[need_dict[num]], need_dict[num])
        continue
    else:
	need_dict[need] = i
#    print need_dict
