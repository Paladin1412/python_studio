# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author；鸿
'''高阶函数map'''
#高阶函数map初级，将列表每个元素求平方
def pow(x):
    return x*x
a = [1,2,3,4,5,6,7,8,9]
L = map(pow,a)#L是一个可迭代对象
print(list(L))

#高阶函数map中级，将列表每个元素转为字符串
a = [1,2,3,4,5,6,7,8,9]
L = map(str,a)
print(list(L))

#高阶函数map进阶，将两个列表相加
def f(x,y):
    return x+y
a = [1,2,3,4]
b = [10,20,30]
L = map(f,a,b)
print(list(L))

'''高阶函数reduce'''
from functools import reduce
def sum(x,y):
    return x+y
a=[1,2,3,4,5]
result1=reduce(sum,a)#((((1+2)+3)+4)+5)
print(result1)

def fun(x,y):
    return x*10+y
result2=reduce(fun,a)#((((1*10+2)*10+3)*10+4)*10+5)
print(result2)


'''高阶函数filter'''
def not_odd(x):
    return x%2==1
L = filter(not_odd,[1,2,3,4,5,6,7,8,9])
print(list(L))

def not_emply(x):
    return x and x.strip()
#strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
#注意：该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。
L = filter(not_emply,['A','',None,'B','   ','C'])
print(list(L))


#高阶函数sorted
sort_list = sorted([1,34,56,32.5,0,59,100,-10,-1,-99])#默认顺序排序reverse=False
print(sort_list)

sort_list = sorted([1,34,56,32.5,0,59,100,-10,-1,-99],reverse=True)#逆序
print(sort_list)

sort_list = sorted(['a','b','aba','abc','A','ABC','D','C'])#字符串排序
print(sort_list)

sort_list = sorted(['a','b','aba','abc','A','ABC','D','C'],reverse=True)#字符串排序
print(sort_list)

#对列表的绝对值排序
sort_list = sorted([1,34,56,32.5,0,59,100,-10,-1,-99],key=abs)#默认顺序排序reverse=False
print(sort_list)

#对字符串不区分大小写排序
sort_list = sorted(['A','b','aba','abc','a','ABC','D','C'],key=str.lower)#字符串排序
print(sort_list)

'''匿名函数'''
f = lambda x:x*x#变量f指向这个函数
print(f(3))

f = lambda a,b,c:a+b+c
print(f(1,2,3))

#匿名函数在map高阶函数中使用
L = map(lambda x:x*x,[1,2,3,4,5,6,7,8,9])
print(list(L))

#匿名函数在sorted高阶函数中使用
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
stu1 = Student('zhangsan',21)
stu2 = Student('lisi',32)
stu3 = Student('wangwu',19)

sort_list = sorted([stu1,stu2,stu3],key=lambda x:x.name)#按照name进行排序
for i in sort_list:
    print('name:',i.name,'age:',i.age)

sort_list = sorted([stu1,stu2,stu3],key=lambda x:x.age)#按照age排序
for i in sort_list:
    print('name:',i.name,'age:',i.age)
