#print("Hello,World!")
# 第一个注释
#print("Hello,Python!") # 第二个注释
# 第一个注释
# 第二个注释
'''
第三注释
第四注释
'''
"""
第五注释
第六注释
"""
'''
if True:
    print("True")
else:
    print("False")
'''
'''
str='Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+'你好')
print('------------------------------')
print('hello\nrunoob')
print(r'hello\nrunoob')
'''
#input("\n\n按下 enter 键后退出。")
#import sys;x='runoob';sys.stdout.write(x+'\n')
'''
import sys
x='runoob'
sys.stdout.write(x+'\n')
'''
'''
if expression:
    suite
elif expression:
    suite
else:
    suite
'''
'''
x="a"
y="b"
# 换行输出
print(x)
print(y)
print('---------')
print(x,end=" ")
print(y,end=" ")
print()
'''
'''
import sysprint('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)
'''
'''
from sys import argv,path
print('================python from import===================================')
print('path:',path)
'''
'''
def getPairs(dict):
    for k,v in dict.items():
        print(k,v,sep=':')
'''
'''
a='2.1'
print(int(a))
'''
'''
a='2.1'
print(int(float(a)))
'''
'''
counter=100
miles=1000.0
name="runoob"
print(counter)
print(miles)
print(name)
'''
'''
a,b,c,d=20,5.5,True,4+3j
print(type(a),type(b),type(c),type(d))
'''
'''
a=111
isinstance(a,int)
'''
'''
var1=1
var2=10
print(var1)
print(var2)
'''
'''
a,b,c=1,2,"runoob"
print(a)
print(b)
print(c)
'''
'''
a,b=1,2
print(a)
print(b)
'''
'''
str='Runoob'
print(str)
print(str[0:-1])
print(str[0])
print(str[2:5])
print(str[2:])
print(str*2)
print(str+"TEST")
'''
'''
print('Ru\noob')
print(r'Ru\noob')
'''
'''
word='Python'
print(word[0],word[5])
print(word[-1],word[-6])
'''
'''
list=['abcd',786,2.23,'runoob',70.2]
tinylist=[123,'runoob']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist*2)
print(list+tinylist)
'''
'''
def reverseWords(input):
    inputWords=input.split(" ")
    inputWords=inputWords[-1::-1]
    output=' '.join(inputWords)
    return output
if _name_=="_main_"
    input='I like runoob'
    rw=reverseWords(input)
    print(rw)
'''
'''
tuple=('abcd',786,2.23,'runoob','70.2')
tinytuple=(123,'runoob')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)
'''
'''
student={'Tom','Jim','Mary','Tom','Jack','Rose'}
print(student)
if 'Rose' in student:
    print('Rose 在集合中')
else:
    print('Rose 不在集合中')
a=set('abracadabra')
b=set('alacazam')
print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)
'''
'''
dict={}
dict['one']="1-菜鸟教程"
dict[2]="2-菜鸟工具"
tinydict={'name':'runoob','code':1,'site':'www.runoob.com'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
'''
'''
aTuple=(123,'Google','Runoob','Taobao')
list1=list(aTuple)
print("列表元素:",list1)
str="Hello World"
list2=list(str)
print("列表元素:",list2)
'''
#print chr(0x30),chr(0x31),chr(0x61)
#print chr(48),chr(49),chr(97)
#hex(1L)
'''
def test(*args):
    print(args)
    return args
print(type(test(1,2,3,4)))
'''
'''
def example(d)
    for c in d:
        print(c)
'''
'''
list=['abcd',786,2.23,'runoob',70.2]
print(list[1:3])
print(list[2])
print(list[2:3])
'''
'''
list=['abcd',786,2.23,'runoob',70.2]
print(list[1:3])
print(list[1:0])
print(list[1:1])
print(list[0:1])
'''
#list=['abcd',786,2.23,'runoob',70.2]
#print(arrtest[1:-1])
#print(arrtest[-3:-2])
'''
list=['abcd',786,2.23,'runoob',70.2]
print(list[2])
print(list[2:3])
a=list[2]
b=list[2:3]
print(type(a))
print(type(b))
'''
'''
class father(object):
    pass
class son(father):
    pass
if _name_=='_main_':
    print(type(son())==father)
    print(isinstance(son().father))
    print(type(son()))
    print(type(son))
'''
'''
dict1={'abc':1,"cde":2,"d":4,"c":567,"d":"key1"}
for k,v in dict1.items():
    print(k,":",v)
'''
'''
a=4.7+0.666j
print(a)
print(a.real)
print(a.imag)
print(a.conjugate())
'''
'''
a='python'
d=a[:-1]
print(d)
'''
'''
demo=[1,2,3,4,5,6]
new_demo=demo[1::2]
print(new_demo)
'''
#'''
#def a():
#    '''这是文档字符串'''
#    pass
#print(a._doc_)
#'''
'''
a=21
b=10
c=0
c=a+b
print("1-c的值为:",c)
c=a-b
print("2-c的值为:",c)
c=a*b
print("3-c的值为:",c)
c=a/b
print("4-c的值为:",c)
c=a%b
print("5-c的值为:",c)
a=2
b=3
c=a**b
print("6-c的值为:",c)
a=10
b=5
c=a//b
print("7-c的值为:",c)
'''
'''
a=21
b=10
c=0
if(a==b):
    print("1-a等于b")
else:
    print("1-a不等于b")
if(a!=b):
    print("2-a不等于b")
else:
    print("2-a等于b")
if(a<b):
    print("3-a小于b")
else:
    print("3-a大于等于b")
if(a>b):
    print("4-a大于b")
else:
    print("4-a小于等于b")
a=5
b=20
#a=5;
#b=20;
if(a<=b):
    print("5-a小于等于b")
else:
    print("5-大于b")
if(b>=a):
    print("6-b大于等于a")
else:
    print("6-b小于a")
'''
'''
a=21
b=10
c=0
c=a+b
print("1-c的值为:",c)
c+=a
print("2-c的值为:",c)
c*=a
print("3-c的值为:",c)
c/=a
print("4-c的值为:",c)
c=2
c%=a
print("5-c的值为:",c)
c**=a
print("6-c的值为:",c)
c//=a
print("7-c的值为:",c)
'''
'''
a=0011 1100
b=0000 1101
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
'''
'''
a=60
b=13
c=0
c=a&b
print("1-c的值为:",c)
c=a|b
print("2-c的值为:",c)
c=a^b
print("3-c的值为:",c)
c=~a
print("4-c的值为:",c)
c=a<<2
print("5-c的值为:",c)
c=a>>2
print("6-c的值为:",c)
'''
'''
a=10
b=20
if(a and b):
    print("1-变量a和b都为true")
else:
    print("1-变量a和b有一个不为true")
if(a or b):
    print("2-变量a和b都为true，或其中一个变量为true")
else:
    print("2-变量a和b都不为true")
a=0
if(a and b):
    print("3-变量a和b都为true")
else:
    print("3-变量a和b有一个不为true")
if(a or b):
    print("4-变量a和b都为true,或其中一个变量为true")
else:
    print("4-变量a和b都不为true")
if not(a and b):
    print("5-变量a和b都为false,或其中一个变量为false")
else:
    print("5-变量a和b都为true")
'''
'''
a=10
b=20
#list=[1,2,3,4,5];
list=[1,2,3,4,5]
if(a in list):
    print("1-变量a在给定的列表中list中")
else:
    print("1-变量a不在给定的列表中list中")
if(b not in list):
    print("2-变量b不在给定的列表中list中")
else:
    print("2-变量b在给定的列表中list中")
a=2
if(a in list):
    print("3-变量a在给定的列表中list中")
else:
    print("3-变量a不在给定的列表中list中")
'''
'''
a=20
b=20
if(a is b):
    print("1-a和b有相同的标识")
else:
    print("1-a和b没有相同的标识")
if(id(a)==id(b)):
    print("2-a和b有相同的标识")
else:
    print("2-a和b没有相同的标识")
b=30
if(a is b):
    print("3-a和b有相同的标识")
else:
    print("3-a和b没有相同的标识")
if(a is not b):
    print("4-a和b没有相同的标识")
else:
    print("4-a和b有相同的标识")
'''
'''
a=20
b=10
c=15
d=5
e=0
e=(a+b)*c/d
print("(a+b)*c/d运算结果为:",e)
e=((a+b)*c)/d
print("((a+b)*c)/d运算结果为:",e)
e=(a+b)*(c/d);
print("(a+b)*(c/d)运算结果为:",e)
e=a+(b*c)/d;
print("a+(b*c)/d运算结果为:",e)
'''
#print(0 and 0)
#print( 0 or 0)
#print "round(100.000056,3):",round(100.000056,3)
#print "round(-100.000056,3):",round(-100.000056,3)
'''
a=-1
b=-1.3232
c=b
d=1+1.0j
e=3+4.0j
#print"a的绝对值是:",abs(a)
#print"b的绝对值是:",abs(b)
#print"c的绝对值是:",math.fabs(c)
#print"d的绝对值是:",abs(d)
print(abs(a))
print(abs(b))
#print(fabs(c))
print(abs(d))
'''
'''
import math
print("math.ceil(-45.17):",math.ceil(-45.17))
print("math.ceil(100.12):",math.ceil(100.12))
print("math.ceil(100.72):",math.ceil(100.72))
print("math.ceil(math.pi):",math.ceil(math.pi))
'''
'''
import math
print("math.exp(-45.17):",math.exp(-45.17))
print("math.exp(100.12):",math.exp(100.12))
print("math.exp(100.72):",math.exp(100.72))
print("math.exp(math.pi):",math.exp(math.pi))
'''
'''
import math
print("math.fabs(-45.17):",math.fabs(-45.17))
print("math.fabs(100.12):",math.fabs(100.12))
print("math.fabs(100.72):",math.fabs(100.72))
print("math.fabs(math.pi):",math.fabs(math.pi))
'''
'''
import math
print("math.floor(-45.17):",math.floor(-45.17))
print("math.floor(100.12):",math.floor(100.12))
print("math.floor(100.72):",math.floor(100.72))
print("math.floor(math.pi):",math.floor(math.pi))
'''
'''
import math
print(math.log(math.e))
print(math.log(100,10))
'''
'''
import math
print("math.log(100.12):",math.log(100.12))
print("math.log(100.72):",math.log(100.72))
print("math.log(math.pi):",math.log(math.pi))
'''
'''
import math
print(math.log10(100))
'''
'''
import math
print("math.log10(100.12):",math.log10(100.12))
print("math.log10(100.72):",math.log10(100.72))
print("math.log10(119):",math.log10(119))
print("math.log10(math.pi):",math.log10(math.pi))
'''
'''
import math
print("math.modf(100.12):",math.modf(100.12))
print("math.modf(100.72):",math.modf(100.72))
print("math.modf(119):",math.modf(119))
print("math.modf(math.pi):",math.modf(math.pi))
'''
'''
import math
def is_sqr(x):
    a=math.sqrt(x)
    return int(a)==a
print filter(is_sqr(16),range(1,101))
'''
'''
import math
print("101-200之间的素数是:",end="")
for i in range(100,201):
    for j in range(2,int(math.sqrt(i))):
        if(i%j==0):break
    else:
        print("",i,end="")
'''
'''
import math
print("101-200之间的素数是:",end="")
for i in range(100,201):
    for j in range(2,int(math.sqrt(i))):
        if(i%j==0):break
    else:
        print("",i,end="")
else:
    print()
'''
'''
for i in range(0,6):
    print(i,end=" ")
'''
'''
for i in range(0,3):
    print(i,end='')
'''
'''
for i in range(0,6):
    print(i,end="")
'''
'''
print() 
'''
'''
import random
print("从range(100)返回一个随机数:",random.choice(range(100)))
print("从列表中[1,2,3,5,9])返回一个随机元素:",random.choice([1,2,3,5,9]))
print("从字符串中'Runoob'返回一个随机字符:",random.choice('Runoob'))
'''
'''
import random
print("从range(100)返回一个随机数:",random.choice(range(100)))
print("从列表中[1,2,3,5,9]返回一个随机元素:",random.choice([1,2,3,5,9]))
print("从字符串中'Runoob'返回一个随机字符:",random.choice('Runoob'))
'''
#print(randrange(10))
'''
import random
print("randrange(1,100,2):",random.randrange(1,100,2))
print("randrange(100):",random.randrange(100))
'''
'''
import random
print(random.randrange(0,100,2))
print(random.randrange(0,100,4))
print(random.randrange(1,100,3))
'''
'''
import random
print("random() : ",random.random())
print("random() : ",random.random())
'''
'''
import random
print("random():",random.random())
print("random():",random.random())
'''
'''
import random
a=random.uniform(10,100)
print(a)
a=int(random.uniform(10,100))
print(a)
'''
'''
import random
print((random.random()*21)+100)
print(random.uniform(100,101))
'''
'''
import random
listb={1:'张三',2:'李四',3:'王五',4:'赵六',5:'王麻子',6:'包子',7:'豆浆'}
lista={1:'张三',2:'李四',3:'王五',4:'赵六',5:'王麻子',6:'包子',7:'豆浆'}
for c in listb.keys():
    a=random.sample(lista.keys(),1)
    b=a[0]
    print(lista[b])
    del lista[b]
    print(lista)
'''
'''
import random
n=0
while n<5:
    a=random.randint(0,10)
    b=int(input("请输入一个整数(0-10):"))
    if a==b:
        print("恭喜您猜对了!",sep='')
        break
    elif b>a:
        print("您猜大了,请重新猜吧!",sep='')
        print("答案是:",a,sep='')
    elif a>b:
        print("您猜小了,请重新猜吧!")
        print("答案是:",a,sep='')
    n+=1
else:
    print("您已经输入5次了!",sep='')
'''
'''
import random
random.seed()
print("使用默认种子生成随机数:",random.random())
print("使用默认种子生成随机数:",random.random())
random.seed(10)
print("使用整数10种子生成随机数:",random.random())
random.seed(10)
print("使用整数10种子生成随机数:",random.random())
random.seed("hello",2)
print("使用字符串种子生成随机数:",random.random())
'''
'''
import random
#list=[20,16,10,5];
list=[20,16,10,5]
random.shuffle(list)
print("随机排序列表:",list)
random.shuffle(list)
print("随机排序列表:",list)
'''
'''
import random
print("uniform(5,10)的随机浮点数:",random.uniform(5,10))
print("uniform(7,14)的随机浮点数:",random.uniform(7,14))
'''
'''
import random
print(round(random.uniform(5,10),2))
'''
'''
import math
print("acos(0.64):",math.acos(0.64))
print("acos(0):",math.acos(0))
print("acos(-1):",math.acos(-1))
print("acos(1):",math.acos(1))
'''
'''
import math
print("asin(0.64):",math.asin(0.64))
print("asin(0):",math.asin(0))
print("asin(-1):",math.asin(-1))
print("asin(1):",math.asin(1))
'''
'''
import math
print("atan(0.64):",math.atan(0.64))
print("atan(0):",math.atan(0))
print("atan(10):",math.atan(10))
print("atan(-1):",math.atan(-1))
print("atan(1):",math.atan(1))
'''
'''
import math
print("atan2(-0.50,-0.50):",math.atan2(-0.50,-0.50))
print("atan2(0.50,0.50):",math.atan2(0.50,0.50))
print("atan2(5,5):",math.atan2(5,5))
print("atan2(-10,10):",math.atan2(-10,10))
print("atan2(10,20):",math.atan2(10,20))
'''
'''
import math
print("cos(3):",math.cos(3))
print("cos(-3):",math.cos(-3))
print("cos(0):",math.cos(0))
print("cos(math.pi):",math.cos(math.pi))
print("cos(2*math.pi):",math.cos(2*math.pi))
'''
'''
import math
print("hypot(3,2):",math.hypot(3,2))
print("hypot(-3,3):",math.hypot(-3,3))
print("hypot(0,2):",math.hypot(0,2))
'''
'''
import math
print("sin(3):",math.sin(3))
print("sin(-3):",math.sin(-3))
print("sin(0):",math.sin(0))
print("sin(math.pi):",math.sin(math.pi))
print("sin(math.pi/2):",math.sin(math.pi/2))
'''
'''
import math
print("tan(3):",math.tan(3))
print("tan(-3):",math.tan(-3))
print("tan(0):",math.tan(0))
print("tan(math.pi):",math.tan(math.pi))
print("tan(math.pi/2):",math.tan(math.pi/2))
print("tan(math.pi/4):",math.tan(math.pi/4))
'''
'''
import math
print("radians(3):",math.radians(3))
print("radians(-3):",math.radians(-3))
print("radians(0):",math.radians(0))
print("radians(math.pi):",math.radians(math.pi))
print("radians(math.pi/2):",math.radians(math.pi/2))
print("radians(math.pi/4):",math.radians(math.pi/4))
'''
'''
import operator
print(operator.gt(1,2))
print(operator.ge(1,2))
print(operator.eq(1,2))
print(operator.le(1,2))
print(operator.lt(1,2))
'''
'''
var='1234'
num=int(var)
print(num)
'''
'''
var='1234'
num_list=list(var)
print(num_list)
'''
'''
var='1234'
num_list=list(var)
import numpy as np
num_array=np.array(num_list)
print(num_array)
'''
'''
var1='Hello World!'
var2="Runoob"
print(var1)
print(var2)
'''
'''
var1='Hello World!'
var2="Runoob"
print("var1[0]:",var1[0])
print("var2[1:5]:",var2[1:5])
'''
'''
var1='Hello World!'
print("已更新字符串:",var1[:6]+'Runoob!')
'''
'''
print(r'\n')
print(R'\n')
'''
'''
a="Hello"
b="Python"
print("a+b输出结果:",a+b)
print("a*2输出结果:",a*2)
print("a[1]输出结果:",a[1])
print("a[1:4]输出结果:",a[1:4])
if("H" in a):
    print("H在变量a中")
else:
    print("H不在变量a中")
if("M" not in a):
    print("M不在变量a中")
else:
    print("M在变量a中")
print(r'\n')
print(R'\n')
'''
#print("我叫 %s 今年 %d 岁!"%('小明',10))
#print("我叫%s今年%d岁!"%('小明',10))
'''
str="this is string example from runoob....wow!!!"
print("str.capitalize():",str.capitalize())
'''
'''
str="[www.runoob.com]"
print("str.center(40,'*'):",str.center(40,'*'))
'''
'''
str="www.runoob.com"
sub='o'
print("str.count('o'):",str.count(sub))
sub='run'
print("str.count('run',0,10):",str.count(sub,0,10))
'''
'''
str="www.runoob.com"
sub='o'
print("str.count('run',0,10):",str.count(sub,0,10))
'''
'''
str="www.aaaaaaacom"
sub='a'
print("str.count('run',0,10):",str.count(sub,0,10))
'''
'''
Str='abcde'
suffix='a'
print(Str.endswith(suffix,0,2))
suffix='c'
print(Str.endswith(suffix,0,2))
'''
'''
str_1=input("输入一个字符串:")
len1=len(str_1)-1
str_list=[]
while(len1>=0):
    str_list.append(str_1[len1])
    len1=len1-1
print(''.join(str_list))
'''
'''
n=input("")
s="零一二三四五六七八九"
for c in "0123456789":
    n=n.replace(c,s[eval(c)])
print(n)
'''
'''
str1="this ibs"
str2="bs"
print(str1.rfind(str2,0,6))
print(str1.find(str2,0,6))
str3="thi"
print(str1.rfind(str3,0,6))
print(str1.find(str3,0,6))
'''
'''
str="this is string example....wow!!!"
print(str.startswith('this',0,15))
print(str.startswith('example',1,15))
'''
'''
str="123abcrunoob321"
print(str.strip('12'))
'''
'''
s1="I'm a good student."
s2=s1.partition('good')
s3=s1.partition('abc')
print(s1)
print(s2)
print(s3)
'''
'''
var='菜鸟教程'
list=[]
list=[i for i in var]
print(list)
'''
'''
var='菜鸟教程'
list=[]
list=[i for i in var]
var1=','.join(list)
print(var1)
'''
'''
var='菜鸟教程'
tup=tuple(var)
print(tup)
'''
'''
for x in [1,2,3]:
    print(x,end="")
'''
'''
list1,list2=['Google','Runoob','Taobao'],[456,700,200]
print(list1)
print(list2)
'''
'''
language=['French','English','German']
language_tuple=('Spanish','Portuguese')
language_set={'Chinese','Japanese'}
language.extend(language_tuple)
print('新列表:',language)
language.extend(language_set)
print('新列表:',language)
'''
'''
a=[[0,1],[1,2],[2,3]]
a.insert(2,a[1])
a.append(a[3])
print(a)
a[1][1]=0
a[4][1]=4
print(a)
'''
'''
p=lambda x,y:x+y
print(p(4,6))
'''
'''
a=lambda x:x*x
print(a(3))
'''
'''
a=lambda x,y,z:(x+8)*y-z
print(a(5,6,8))
'''
'''
a=[[1,3],[3,2],[2,4],[1,2],[1,5],[2,5]]
print(a)
a.sort()
print(a)
'''
#name_list=["唱","跳","rap","篮球"]
#num_list=[1,7,6,3,10]
'''
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
'''
'''
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)
'''
'''
name_list.reverse()
num_list.reverse()
print(name_list)
print(num_list)
'''
'''
arr=[{'name':'wcl','age':23},{'name':'wjy','age':14}]
arr2=arr.copy()
del arr[1]
#arr[0]['age']=18
arr2[0]['age']=18
print('arr',arr)
print('arr2',arr2)
'''
'''
import copy
a=[1,2,3,4]
b=a
d=copy.copy(a)
b[0]='b'
print(a,b,d)
print(id(a),id(b),id(d))
'''
'''
li=[1,2,3,4,5,6,7,8,9]
print([x**2 for x in li])
print([x**2 for x in li if x>5])
print(dict([(x,x*10) for x in li]))
print([(x,y) for x in range(10) if x%2 if x>3 for y in range(10) if y>7 if y!=8])
vec=[2,4,6]
vec2=[4,3,-9]
sq=[vec[i]+vec2[i] for i in range(len(vec))]
print(sq)
print([x*y for x in [1,2,3] for y in [1,2,3]])
testList=[1,2,3,4]
def mul2(x):
    return x*2
print([mul2(i) for i in testList])
'''
'''
tup=('Google','Runoob',1997,2000)
print(tup)
del tup;
print("删除后的元组tup:")
print(tup)
'''
'''
import collections
User=collections.namedtuple('User',['name','age','id'])
#User=collections.namedtuple('User','name age id')
user=User('tester','22','464643123')
print(user)
'''
'''
t1=(1,2,"3")
t2=("4",5,["d1","d2"])
print("t1=",t1)
print("t2=",t2)
'''
'''
t1=(1,2,"3")
t2=("4",5,["d1","d2"])
print("t1=",t1)
print("t2=",t2)
t1=t1+t2
t1[5].append("d3")
print("t1[5]=",t1[5])
print("t2=",t2)
'''
'''
tuple1=(1,2,4,5)
print(tuple1[:2])
print(tuple1[2:])
tuple2=tuple1[:2]+(3,)+tuple1[2:]
print(tuple2)
'''
'''
tup=(4,5,6,7,8)
tup=('谁','说','元','组','不','能','改')
print(tup)
tup=(4,6,7,8,9,10,0)
tup=list(tup)
list2=['谁','说','元','组','不','能','改']
for i in range(7):
    tup[i]=list2[i]
print(tup)
'''
'''
dict={'Name':'Runoob','Age':7,'Class':'First'}
print("dict['Name']:",dict['Name'])
print("dict['Age']:",dict['Age'])
'''
'''
dict={'Name':'Runoob','Age':7,'Class':'First'}
print("dict['Alice']:",dict['Alice'])
'''
'''
dict={'Name':'Runoob','Age':7,'Class':'First'}
dict['Age']=8
dict['School']="菜鸟教程"
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
'''
'''
dict={'Name':'Runoob','Age':7,'Class':'First'}
del dict['Name']
dict.clear()
print("dict['Age']:",dict['Age'])
print("dict['School']:",dict['School'])
#del dict
#print("dict['Age']:",dict['Age'])
#print("dict['School']:",dict['School'])
'''
'''
dict={'Name':'Runoob','Age':27}
print("Age值为:%s"%dict.get('Age'))
print("Sex值为:%s"%dict.get('Sex',"NA"))
'''
'''
dict={'Name':'Runoob','Age':7}
print("Value:%s"%dict.items())
'''
'''
dict={'Name':'Runoob','Age':7}
for i,j in dict.items():
    print(i,":\t",j)
'''
'''
d={1:"a",2:"b",3:"c"}
result=[]
for k,v in d.items():
    result.append(k)
    result.append(v)
print(result)
'''
'''
dict={'Name':'Runoob','Age':7}
print("Age键的值为:%s"%dict.setdefault('Age',None))
print("Sex键的值为:%s"%dict.setdefault('Sex',None))
print("新字典为:",dict)
'''
'''
dict={'Name':'Runoob','Age':7}
dict2={'Sex':'female'}
dict.update(dict2)
print("更新字典dict:",dict)
'''
'''
dict={'Sex':'female','Age':7,'Name':'Zara'}
print("字典所有值为:",list(dict.values()))
'''
'''
students={}
write=1
while write:
    name=str(input('输入名字:'))
    grade=int(input('输入分数:'))
    students[str(name)]=grade
    write=int(input('继续输入?\n 1/继续 0/退出'))
print('name  rate'.center(20,'-'))
for key,value in students.items():
    if value>=90:
        print('%s %s  A'.center(20,'-')%(key,value))
    elif 89>value>=60:
        print('%s %s  B'.center(20,'-')%(key,value))
    else:
        print('%s %s  C'.center(20,'-')%(key,value))
'''
'''
students={}
write=1
while write:
    name=str(input('输入名字:'))
    grade=int(input('输入分数:'))
    students[str(name)]=grade
    write=int(input('继续输入?\n 1/继续 0/退出'))
print('name  rate'.center(20,'-'))
for key,value in students.items():
    if value>=90:
        print('%s %s A'.center(20,'-')%(key,value))
    elif 89>value>=60:
        print('%s %s B'.center(20,'-')%(key,value))
    else:
        print('%s %s C'.center(20,'-')%(key,value))
'''
'''
dic={'a':1,'b':2,'c':3,}
reverse={v:k for k,v in dic.items()}
print(dic)
print(reverse)
'''
'''
dic={'a':1,'b':2,'c':3}
reverse={v:k for k,v in dic.items()}
print(dic)
print(reverse)
'''
'''
b={'a':'runoob','b':'google'}
for i in b.values():
    print(i)
for c in b.keys():
    print(c)
'''
'''
prices={'A':123,'B':450.1,'C':12,'E':444,}
max_prices=max(zip(prices.values(),prices.keys()))
print(max_prices)
'''
'''
prices={'A':123,'B':450.1,'C':12,'E':444}
max_prices=max(zip(prices.values(),prices.keys()))
print(max_prices)
'''
'''
dict_0={'color':'green','points':5}
dict_1={'color':'yellow','points':10}
dict_2={'color':'red','points':15}
lists=[dict_0,dict_1,dict_2]
for dict in lists:
    print(dict)
'''
'''
fruits={"apple","banana","cherry"}
fruits.add("orange")
print(fruits)
'''
'''
fruits={"apple","banana","cherry"}
fruits.clear()
print(fruits)
'''
'''
fruits={"apple","banana","cherry"}
x=fruits.copy()
print(x)
'''
'''
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
z=x.difference(y)
print(z)
'''
'''
x={"apple","banana","cherry"}
y={"google","microsoft","apple"}
x.difference_update(y)
print(x)
'''
'''
fruits={"apple","banana","cherry"}
fruits.discard("banana")
print(fruits)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.intersection(y)
print(z)
'''
'''
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
result=x.intersection(y,z)
print(result)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
x.intersection_update(y)
print(x)
'''
'''
x={"a","b","c"}
y={"c","d","e"}
z={"f","g","c"}
x.intersection_update(y,z)
print(x)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","facebook"}
z=x.isdisjoint(y)
print(z)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.isdisjoint(y)
print(z)
'''
'''
x={"a","b","c"}
y={"f","e","d","c","b","a"}
z=x.issubset(y)
print(z)
'''
'''
x={"a","b","c"}
y={"f","e","d","c","b"}
z=x.issubset(y)
print(z)
'''
'''
x={"f","e","d","c","b","a"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)
'''
'''
x={"f","e","d","c","b"}
y={"a","b","c"}
z=x.issuperset(y)
print(z)
'''
'''
fruits={"apple","banana","cherry"}
fruits.pop()
print(fruits)
'''
'''
fruits={"apple","banana","cherry"}
x=fruits.pop()
print(x)
print(fruits)
'''
'''
fruits={"apple","banana","cherry"}
fruits.remove("banana")
print(fruits)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.symmetric_difference(y)
print(z)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
x.symmetric_difference_update(y)
print(x)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
z=x.union(y)
print(z)
'''
'''
x={"a","b","c"}
y={"f","d","a"}
z={"c","d","e"}
result=x.union(y,z)
print(result)
'''
'''
x={"apple","banana","cherry"}
y={"google","runoob","apple"}
x.update(y)
print(x)
'''
'''
age=int(input("请输入你家狗狗的年龄:"))
print("")
if age<=0:
    print("你是在逗我吧!")
elif age==1:
    print("相当于14岁的人。")
elif age==2:
    print("相当于22岁的人。")
elif age>2:
    human=22+(age-2)*5
    print("对应人类年龄:",human)
input("点击enter键退出")
'''
'''
number=7
guess=-1
print("数字猜谜游戏!")
while guess!=number:
    guess=int(input("请输入你猜的数字:"))
    if guess==number:
        print("恭喜,你猜对了!")
    elif guess<number:
        print("猜的数字小了...")
    elif guess>number:
        print("猜的数字大了...")
'''
'''
num=int(input("输入一个数字:"))
if num%2==0:
    if num%3==0:
        print("你输入的数字可以整除2和3")
    else:
        print("你输入的数字可以整除2,但不能整除3")
else:
    if num%3==0:
        print("你输入的数字可以整除3,但不能整除2")
    else:
        print("你输入的数字不能整除2和3")
'''
'''
import random
x=random.choice(range(100))
y=random.choice(range(200))
if x>y:
    print('x:',x)
elif x==y:
    print('x+y:',x+y)
else:
    print('y:',y)
'''
'''
print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age=int(input("请输入您家狗的年龄:"))
        print(" ")
        age=float(age)
        if age<0:
            print("您在逗我?")
        elif age==1:
            print("相当于人类14岁")
            break
        elif age==2:
            print("相当于人类22岁")
            break
        else:
            human=22+(age-2)*5
            print("相当于人类:",human)
            break
    except ValueError:
        print("输入不合法,请输入有效年龄")
input("点击enter键退出")
'''
'''
print('二、数字猜谜游戏')
print('数字猜谜游戏!')
a=1
i=0
while a!=20:
    a=int(input('请输入你猜的数字:'))
    i+=1
    if a==20:
        if i<3:
            print('真厉害,这么快就猜对了!')
        else:
            print('总算猜对了，恭喜恭喜!')
    elif a<20:
        print('你猜的数字小了,不要灰心,继续努力!')
    else:
        print('你猜的数字大了,不要灰心,继续加油!')
'''
'''
print("=======欢迎进入狗狗年龄对比系统========")
control="N"
while control=="N":
    try:
        age=int(input("请输入您家狗的年龄:"))
        #print(" ")
        age=float(age)
        if age<0:
            print("您在逗我?")
        elif age==1:
            print("相当于人类14岁")
            #break
        elif age==2:
            print("相当于人类22岁")
            #break
        else:
            human=22+(age-2)*5
            print("相当于人类:",human)
            #break
    except ValueError:
        print("输入不合法,请输入有效年龄")
    print("")
    control=input("退出(Y/N)?")
    print("")
input("点击enter键退出")
'''
'''
a='None'
if a:
    print(11)
else:
    print(22)
'''
'''
print('----欢迎使用BMI计算程序----')
name=input('请输入您的姓名:')
height=eval(input('请键入您的身高(m):'))
weight=eval(input('请键入您的体重(kg):'))
gender=input('请键入你的性别(F/M)')
BMI=float(float(weight)/(float(height)**2))
if BMI<=18.4:
    print('姓名:',name,'身体状态:偏瘦')
elif BMI<=23.9:
    print('姓名:',name,'身体状态:正常')
elif BMI<=27.9:
    print('姓名:',name,'身体状态:超重')
elif BMI>=28:
    print('姓名:',name,'身体状态:肥胖')
import time
nowtime=(time.asctime(time.localtime(time.time())))
if gender=='F':
    print('感谢',name,'女士在',nowtime,'使用本程序,祝您身体健康!')
if gender=='M':
    print('感谢',name,'先生在',nowtime,'使用本程序,祝您身体健康!')
'''
'''
name="pag"
if name=="pag":
    print(name=="pag")
if (name=="pag"):{
    print(name=="pag")
}
'''
'''
import random
x=random.choice(range(100))
y=random.choice(range(100))
b,c=x,y
a=1
print(x,y)
while x!=y:
    if x>y:
        print('x:',x)
    elif x==y:
        print('x+y:',x+y,'totall cal ',a,'times')
    else:
        print('y:',y)
    x=random.choice(range(100))
    y=random.choice(range(100))
    a=a+1
print('initialized data:',b,c,'x+y:',x+y,'total cal ',a,'times')
'''
'''
import random
x=random.choice(range(100))
y=random.choice(range(100))
b,c=x,y
a=1
print(x,y)
while x!=y:
    if x>y:
        print('x:',x)
    elif x==y:
        print('x+y:',x+y,'total cal ',a,'times')
        break
    else:
        print('y:',y)
    x=random.choice(range(100))
    y=random.choice(range(100))
    a=a+1
print('initialized data:',b,c,'x+y:',x+y,'total cal ',a,'times')
'''
'''
import random
a=0
while True:
    x=random.choice(range(100))
    y=random.choice(range(100))
    a=a+1
    if x>y:
        print(x,'>',y)
    elif x<y:
        print(x,'<',y)
    else:
        print('x=y=',x,'total cal ',a,'times')
        break
'''
'''
if 2>1 and 3>2 and 4>3 and \
    5>4 and 6>5 and 7>6 and \
    8>7:
    print("OK")
'''
'''
if 2>1 and 3>2 and 4>3 and 5>4 and 6>5 and 7>6 and 8>7:
    print("OK")
'''
'''
n=100
sum=0
counter=1
while counter<=n:
    sum=sum+counter
    counter+=1
print("1到%d之和为:%d"%(n,sum))
'''
'''
var=1
while var==1:
    num=int(input("输入一个数字:"))
    print("你输入的数字是:",num)
print("Good bye!")
'''
'''
flag=1
while(flag):print('欢迎访问菜鸟教程!')
print("Good bye!")
'''
'''
languages=["C","C++","Perl","Python"]
for x in languages:
    print(x)
'''
'''
for i in range(0,10):
    if i>10:
        break;
else:
    print("hello world");
'''
'''
for i in range(0,10):
    if i>5:
        break;
else:
    print("hello world");
'''
'''
sites=["Baidu","Google","Runoob","Taobao"]
for site in sites:
    if site=="Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 "+site)
else:
    print("没有循环数据!")
print("完成循环!")
'''
'''
for letter in 'Runoob':
    if letter=='b':
        break
    print('当前字母为:',letter)
var=10
while var>0:
    print('当期变量值为:',var)
    var=var-1
    if var==5:
        break
print("Good bye!")
'''
'''
for letter in 'Runoob':
    if letter=='o':
        continue
    print('当前字母:',letter)
var=10
while var>0:
    var=var-1
    if var==5:
        continue
    print('当前变量值:',var)
print("Good bye!")
'''
'''
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,'等于',x,'*',n//x)
            break
    else:
        print(n,' 是质数')
'''
'''
for letter in 'Runoob':
    if letter=='o':
        pass
        print('执行pass块')
    print('当前字母:',letter)
print("Good bye!")
'''
'''
n=0
sum=0
for n in range(0,101):
    sum+=n
print(sum)
'''
'''
i=1
while i<=9:
    j=1
    while j<=i:
        mut=j*i
        print("%d*%d=%d"%(j,i,mut),end=" ")
        j+=1
    print("")
    i+=1
'''
'''
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print('\r')
'''
'''
print(sum(range(101)))
'''
'''
if a>1:
    pass
'''
'''
while True:
    number=input('请输入一个整数(输入Q退出程序):')
    if number in ['q','Q']:
        break
    elif not number.isdigit():
        print('您的输入有误!只能输入整数(输入Q退出程序)!请重新输入')
        continue
    else:
        number=int(number)
        print('十进制-->十六进制:%d->0x%x'%(number,number))
        print('十进制-->  八进制:%d->0o%o'%(number,number))
        print('十进制-->  二进制:%d->'%number,bin(number))
'''
'''
def paixu(li):
    max=0
    for ad in range(len(li)-1):
        for x in range(len(li)-1-ad):
            if li[x]>li[x+1]:
                max=li[x]
                li[x]=li[x+1]
                li[x+1]=max
            else:
                max=li[x+1]
    print(li)
paixu([41,23344,9353,5554,44,7557,6434,500,2000])
'''
'''
import random
print(random.randint(1,5))
'''
'''
import random
while 1:
    s=int(random.randint(1,3))
    if s==1:
        ind="石头"
    elif s==2:
        ind="剪刀"
    elif s==3:
        ind="布"
    m=input('输入石头,剪刀,布,输入end结束游戏:')
    blist=['石头','剪刀','布']
    if (m not in blist) and (m!='end'):
        print("输入有误,重试:")
    elif (m=='end') and (m not in blist):
        print(ind)
        print("\n游戏退出")
        break
    elif m==ind:
        print("平")
    elif (m=='石头' and ind=='剪刀') or (m=='剪刀' and ind=='布') or (m=='布' and ind=='石头'):
        print("电脑出了: "+ind+",你赢了!")
    else:
        print("电脑出了: "+ind+",你输了!")
'''
'''
for i in range(9,0,-1):
    for j in range(1,i):
        print("\t",end="")
    for k in range(i,10):
        print("%dx%d=%d"%(i,k,k*i),end="\t")
    print()
'''
'''
import random
t1="开始游戏"
t2="结束游戏"
print(t1.center(50,"*"))
data1=[]
money=int(input("输入投入的金额:"))
print("你现在余额为:%d元"%money)
while 1:
    for i in range(6):
        n=random.choice([0,1])
        data1.append(n)
    if money<2:
        print("你的余额不足,请充值")
        m=input("输入投入的金额:")
        if int(m)==0:
            break
        else:
            money=int(m)
    while 1:
        j=int(input("输入购买彩票数量"))
        if money-j*2<0:
            print("购买后余额不足,请重新输入")
        else:
            money=money-j*2
            print("你现在余额为:%d元"%money)
            break
    print("提示:中奖数据有六位数,每位数为0或者1")
    n2=input("请猜测中奖数据:(输入的数字为0或1)")
    print(str(data1))
    f=[]
    for x in n2:
        f.append(x)
    f1=str(f)
    f2=f1.split("'")
    f3="".join(f2)
    print("你猜测的数据为:",f3)
    if f3==str(data1):
        print("中奖数字为:",data1)
        print("恭喜你中大奖啦")
        money=money+j*100
        print("你现在余额为:%d元"%money)
    else:
        print("中奖数字为:",data1)
        print("没有中奖,请继续加油")
    con=input("请问还要继续么?结束请输入no,继续请任意输入字符:")
    if con=="no":
        break
    data1=[]
print(t2.center(50,"*"))
print("你的余额为:%d元"%money)
'''
'''
a=[1,5,4,2,2,21,12,7,0]
b=list(set(a))
c=[]
for j in b:
    for i in a:
        if i==j:
            c.append(i)
print(c)
print(set(a))
print(list(set(a)))
print(b)
'''
'''
a=[1,2,5,8,3,6,6,6,6,6]
a.sort()
print(a)
'''
'''
for i in list(range(1000,2500)):
    num2=i*4
    a=i//1000
    b=i%1000//100
    c=i%1000%100//10
    d=i%10
    e=num2//1000
    f=num2%1000//100
    g=num2%1000%100//10
    h=num2%10
    if a==h:
        if b==g:
            if c==f:
                if d==e:
                    print(num2,end=',')
'''
'''
import sys
list=[1,2,3,4]
it=iter(list)
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
'''
'''
class MyNumbers:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        x=self.a
        self.a+=1
        return x
myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
'''
'''
class MyNumbers:
    def _iter_(self):
        self.a=1
        return self
    def _next_(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration
myclass=MyNumbers()
myiter=iter(myclass)
for x in myiter:
    print(x)
'''
'''
import sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if (counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
f=fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
'''
'''
class Fab(object):
    def _init_(self,max):
        self.max=max
        self.n,self.a,self.b=0,0,1
    def _iter_(self):
        return self
    def next(self):
        if self.n<self.max:
            r=self.b
            self.a,self.b=self.b,self.a+self.b
            self.n=self.n+1
            return r
        raise StopIteration()
for n in Fab(5):
    print(n)
'''
'''
def fab(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
for x in fab(1000):
    #print(x)
    print(x,end='')
'''
'''
def get():
    m=0
    n=2
    l=['s',1,3]
    k={1:1,2:2}
    p=('2','s','t')
    while True:
        m+=1
        yield m
        yield m,n,l,k,p
it=get()
print(next(it))
print(next(it))
print(next(it))
print(type(next(it)))
'''
'''
def get():
    m=0
    n=2
    l=['s',1,3]
    k={1:1,2:2}
    p=('2','s','t')
    while True:
        m+=1
        yield m
        yield m,n,l,k,p
it=get()
print(next(it))
print(next(it))
print(next(it))
print(type(next(it)))
print(type(next(it)))
'''
'''
class Fibonacci:
    def _init_(self,count):
        self.count=count
    def _iter_(self):
        self.i=0
        self.a,self.b=0,1
        return self
    def _next_(self):
        if self.i<self.count:
            self.i+=1
            a_old=self.a
            self.a,self.b=self.b,self.a+self.b
            return a_old
        else:
            raise StopIteration
for i in Fibonacci(10):
    print(i,end=" ")
'''
'''
def area(width,height):
    return width*height
def print_welcome(name):
    print("Welcome",name)
print_welcome("Runoob")
w=4
h=5
print("width=",w," height=",h," area=",area(w,h))
'''
'''
def printme(str):
    print(str)
    return
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
'''
'''
def ChangeInt(a):
    a=10
b=2
ChangeInt(b)
print(b)
'''
'''
def changeme(mylist):
    mylist.append([1,2,3,4])
    print("函数内取值:",mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print("函数外取值: ",mylist)
'''
'''
def printme(str):
    print(str)
    return
printme(str="菜鸟教程")
'''
'''
def printinfo(name,age):
    print("名字: ",name)
    print("年龄: ",age)
printinfo(age=50,name="runoob")
'''
'''
def printinfo(name,age=35):
    print("名字: ",name)
    print("年龄: ",age)
    return
printinfo(age=50,name="runoob")
print("------------------------")
printinfo(name="runoob")
'''
'''
def printinfo(arg1,*vartuple):
    print("输出: ")
    print(arg1)
    print(vartuple)
printinfo(70,60,50)
'''
'''
def printinfo(arg1,*vartuple):
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return
printinfo(10)
printinfo(70,60,50)
'''
'''
def printinfo(arg1,**vardict):
    print("输出: ")
    print(arg1)
    print(vardict)
printinfo(1,a=2,b=3)
'''
'''
sum=lambda arg1,arg2:arg1+arg2
print("相加后的值为: ",sum(10,20))
print("相加后的值为: ",sum(20,20))
'''
'''
def sum(arg1,arg2):
    total=arg1+arg2
    print("函数内: ",total)
    return total
total=sum(10,20)
print("函数外: ",total)
'''
'''
def printinfo(age=35,name):
    print("名字: ",name)
    print("年龄: ",age)
    return
printinfo(age=50,name="runoob")
printinfo(name="runoob")
'''
'''
def changeme(mylist):
    mylist=[1,2,3,4]
    print("函数内取值: ",mylist)
    return
mylist=[10,20,30]
changeme(mylist)
print("函数外取值: ",mylist)
'''
'''
x=int(3.3)
print(x)
'''
'''
x=int(3.3)
x=0
def outer():
    x=1
    def inner():
        x=2
        print(x)
    inner()
outer()
'''
'''
x=int(3.3)
x=0
def outer():
    x=1
    def inner():
        i=2
        print(x)
    inner()
outer()
'''
'''
x=int(3.3)
x=0
def outer():
    o=1
    def inner():
        i=2
        print(x)
    inner()
outer()
'''
'''
x=int(3.3)
g=0
def outer():
    o=1
    def inner():
        i=2
        print(x)
    inner()
outer()
'''
'''
a=10
def sum(n):
    n+=a
    print('a=',a,end=',')
    print('n=',n)
sum(3)
'''
'''
a=10
def sum(n):
    global a
    n+=a
    a=11
    print('a=',a,end=',')
    print('n=',n)
sum(3)
print('外a=',a)
'''
'''
def hello():
    print("Hello,world!")
def execute(f):
    f()
execute(hello)
'''
'''
def add(a,b):
    "这是add函数文档"
    return a+b
print(add.__doc__)
'''
'''
#def function():
    #'''
       #say something here!
    #'''
    #pass
#print(function.__doc__)
'''
'''
'''
def function():
    """
       say something here!
    """
    pass
print(function.__doc__)
'''
'''
'''
#def printMax(x,y):
    #'''
       #打印两个数中的最大值。
       #两个值必须都是在整形数。
    #'''
    #x=int(x)
    #y=int(y)
    #if x>y:
        #print(x,'最大')
    #else:
        #print(y,'最大')
#printMax(3,5)
#print(printMax.__doc__)
'''
def fun(a,b):
    return a,b,a+b
print(fun(1,2))
'''
'''
def log(pr):
    def wrapper():
        print("**********")
        return pr()
    return wrapper
@log
def pr():
    print("我是小小洋")
pr()
'''
'''
a=10
def test():
    b=a+2
    print(b)
test()
'''
'''
a=10
def test():
    a=a+1
    print(a)
test()
'''
'''
num=20
def outer():
    num=10
    def inner():
        global num
        print(num)
        num=100
        print(num)
    inner()
    print(num)
outer()
print(num)
'''
'''
class demo:
    name=""
    def _init_(self):
        self.ex()
        self.start()
    def inputName(self):
        global name
        name=input("输入您的姓名:")
    def getFirstName(self):
        if len(name)<=0:
            x="别闹!请输入姓名!"
            return x
        else:
            x=name[0]
            return x
    def getLastName(self):
        if len(name)<=1:
            y="别闹!长度不够!"
            return y
        else:
            y=name[1:]
            return y
myname=demo()
myname.inputName()
print(myname.getFirstName())
print(myname.getLastName())
'''
'''
def function_demo(param_A:int,param_B:float,param_C:list,param_D:tuple)->dict:
    pass
'''
'''
list=[0,1,2,3,4,5]
list[len(list):]=[6]
print(list)
'''
'''
list=[0,1,2,3,4,5]
list.append(6)
print(list)
'''
'''
a=[1,2,3,4]
b=[5,6,7,8]
c=[9,10,11,12]
t=a,b,c
print(t)
del b[1:4]
print(t)
'''
'''
questions=['name','quest','favorite color']
answers=['qinshihuang','the holy','blue']
for q,a in zip(questions,answers):
    print('what is your %s?it is %s'%(q,a))
    print('what is your {0}?it is {1}'.format(q,a))
'''
'''
import sys
print('命令行参数如下:')
for i in sys.argv:
    print(i)
print('\n\nPython 路径为: ',sys.path,'\n')
'''
'''
if __name__=='__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')
'''
'''
str=input("请输入:");
print("你输入的内容是:",str)
'''
'''
f=open("E:/vscodelearn/tmp/foo.txt","w")
f.write("Python是一个非常好的语言。\n是的,的确非常好!!\n")
f.close()
'''
'''
ff=open("E:/vscodelearn/tmp/fooo.txt","w")
ff.write("C是一个非常好的语言。\n是的,的确非常好!!\n")
ff.close()
'''
'''
f=open("E:/vscodelearn/tmp/foo.txt","r")
str=f.read()
print(str)
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/foo.txt","r")
str=f.readline()
print(str)
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/foo.txt","r")
str=f.readlines()
print(str)
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/foo.txt","r")
for line in f:
    print(line,end='')
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/foooo.txt","w")
num=f.write("Python 是一个非常好的语言。\n是的,的确非常好!!\n")
print(num)
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/fooooo.txt","w")
f.write("Python 是一个非常好的语言。\n是的,的确非常好!!\n")
print(f.write("Python 是一个非常好的语言。\n是的,的确非常好!!\n"))
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/foo1.txt","w")
value=('www.runoob.com',14)
s=str(value)
f.write(s)
f.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob2.txt","r")
print("文件名为:",fo.name)
line=fo.readline()
print("读取的数据为:%s"%(line))
pos=fo.tell()
print("当前位置:%d"%(pos))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob.txt","r")
print("文件名为:",fo.name)
line=fo.readline()
print("读取的数据为:%s"%(line))
pos=fo.tell()
print("当前位置:%d"%(pos))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob3.txt","r")
print("文件名为:",fo.name)
line=fo.read(10)
print("读取的字符串:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob4.txt","r")
print("文件名为:",fo.name)
line=fo.readline()
print("读取的数据为:%s"%(line))
fo.seek(0,0)
line=fo.readline()
print("读取的数据为:%s"%(line))
fo.close()
'''
'''
from urllib import request 
response=request.urlopen("http://www.baidu.com/")
fi=open("project.txt",'w')
page=fi.write(str(response.read()))
fi.close()
'''
'''
a=input('请输入数字:')
print(a*2)
b=int(input('请输入数字:'))
print(b*2)
'''
'''
print('%o'%20)
print('%d'%20)
print('%x'%24)
'''
'''
print('%f'%1.11)
print('%.1f'%1.11)
print('%e'%1.11)
print('%.3e'%1.11)
print('%g'%1111.1111)
print('%.7g'%1111.1111)
print('%.2g'%1111.1111)
'''
'''
print('%s'%'hello world')
print('%20s'%'hello world')
print('%-20s'%'hello world')
print('%.2s'%'hello world')
print('%10.2s'%'hello world')
print('%-10.2s'%'hello world')
'''
'''
print('%.2s'%'hello world')
print('%2s'%'hello world')
'''
'''
f=open("E:/vscodelearn/tmp/runoob7.txt","w+")
'''
'''
f=open("E:/vscodelearn/tmp/runoob7.txt","a+")
f.write("append content")
print(f.tell())
f.seek(0)
print(f.tell())
str=f.read()
print(str)
f.close()
'''
'''
f=open("E:/vscodelearn/tmp/runoob8.txt","w+")
f.write("append content")
print(f.tell())
f.seek(0)
print(f.tell())
str=f.read()
print(str)
f.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob9.txt","wb")
print("文件名为:",fo.name)
fo.flush()
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob9.txt","wb")
print("文件名为:",fo.name)
fid=fo.fileno()
print("文件描述符为:",fid)
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob9.txt","wb")
print("文件名为:",fo.name)
ret=fo.isatty()
print("返回值:",ret)
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob10.txt","r")
print("文件名为:",fo.name)
for index in range(5):
    line=next(fo)
    print("第%d行-%s"%(index,line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob11.txt","r+")
print("文件名为:",fo.name)
line=fo.read(10)
print("读取的字符串:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob12.txt","r+")
print("文件名为:",fo.name)
line=fo.readline()
print("读取第一行%s"%(line))
line=fo.readline(5)
print("读取的字符串为:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob13.txt","r")
print("文件名为:",fo.name)
for line in fo.readlines():
    line=line.strip()
    print("读取的数据为:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob14.txt","r+")
print("文件名为:",fo.name)
line=fo.readline()
print("读取的数据为:%s"%(line))
fo.seek(0,0)
line=fo.readline()
print("读取的数据为:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob15.txt","r+")
print("文件名为:",fo.name)
line=fo.readline()
print("读取的数据为:%s"%(line))
pos=fo.tell()
print("当前位置:%d"%(pos))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob16.txt","r+")
print("文件名:",fo.name)
line=fo.readline()
print("读取行:%s"%(line))
fo.truncate()
line=fo.readlines()
print("读取行:%s"%(line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob16.txt","r+")
print("文件名为:",fo.name)
fo.truncate(10)
str=fo.read()
print("读取数据:%s"%(str))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob17.txt","r+")
print("文件名:",fo.name)
str="6:www.runoob.com"
fo.seek(0,2)
line=fo.write(str+"\n")
fo.seek(0,0)
for index in range(6):
    line=next(fo)
    print("文件行号%d-%s"%(index,line))
fo.close()
'''
'''
fo=open("E:/vscodelearn/tmp/runoob18.txt","w")
print("文件名为:",fo.name)
seq=["菜鸟教程1\n","菜鸟教程2"]
fo.writelines(seq)
fo.close()
'''
'''
def getfile_fix(filename):
    return filename[filename.rfind('.')+1:]
print(getfile_fix('E:/vscodelearn/tmp/runoob19.txt'))
'''
'''
def file_replace(file_name,rep_word,new_word):
    f_read=open(file_name)
    content=[]
    count=0
    for eachline in f_read:
        if rep_word in eachline:
            count=count+eachline.count(rep_word)
            eachline=eachline.replace(rep_word,new_word)
        content.append(eachline)
    decide=input('\n文件%s中共有%s个[%s]\n您确定要把所有的[%s]替换为[%s]吗?\n[YES/NO]:'%(file_name,count,rep_word,rep_word,new_word))
    if decide in ['YES','Yes','yes']:
        f_write=open(file_name,'w')
        f_write.writelines(content)
        f_write.close()
    f_read.close()
file_name=input('请输入文件名:')
rep_word=input('请输入需要替换的单词或字符:')
new_word=input('请输入新的单词或字符:')
file_replace(file_name,rep_word,new_word)
'''
'''
f=open("E:/vscodelearn/tmp/runoob21.txt","w+",encoding='utf-8')
f.write("可以,你做的很好!6666")
s=f.tell()
f.seek(0,0)
str=f.read()
print(s,str,len(str))
'''
'''
with open('E:/vscodelearn/tmp/runoob22.txt','w',encoding='utf-8') as f:
    f.write('test')
with open('E:/vscodelearn/tmp/runoob22.txt','r',encoding='utf-8') as f:
    f.readlines()
'''
'''
try:
    f=open('E:/vscodelearn/tmp/runoob23.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
'''
'''
import os,sys
path="E:/vscodelearn/liebiaomulu"
dirs=os.listdir(path)
for file in dirs:
    print(file)
'''
'''
import os
def Replace(file_name,rep_word,new_word):
    with open(file_name) as f:
        content=[]
        count=0
        for eachline in f:
            if rep_word in eachline:
                count+=eachline.count(rep_word)
                eachline=eachline.replace(rep_word,new_word)
            content.append(eachline)
        decide=input('文件{0}中共有{1}个[{2}]\n您确定要把所有的[{3}]替换为[{4}]吗?\n[YES/NO]:'.fo(file_name,count,rep_word,rep_word,new_word))
        if decide in ['YES','Yes','yes']:
            with open(file_name,'w') as f:
                f.writelines(content)
            print('Succeed!')
        else:
            print('Exit!')
if __name__=='__main__':
    while True:
        file_name=input('请输入文件名:')
        if file_name in os.listdir():
            rep_word=input('请输入需要替换的单词或字符:')
            new_word=input('请输入新的单词或字符:')
            Replace(file_name,rep_word,new_word)
            break
        else:
            print('Do not find such a file {}'.format(file_name))
'''
'''
import sys
sys.stdout=open('E:/vscodelearn/runoob25.txt','w')
print('Hello world')
'''
'''
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye,world!')
'''
'''
for line in open("E:/vscodelearn/tmp/myfile.txt"):
    print(line,end="")
'''
'''
with open("E:/vscodelearn/tmp/myfile2.txt") as f:
    for line in f:
        print(line,end="")
'''
'''
def temp_convert(var):
    try:
        return int(var)
    except {ValueError} as Argument:
        print("参数没有包含数字\n",Argument)
temp_convert("xyz");
'''
'''
def test1():
    print('test1-1')
    print(num)
    print('test2-2')
def test2():
    print('test2-1')
    test1()
    print('test2-2')
def test3():
    try:
        print('test3-1')
        test1()
        print('test3-2')
    except Exception as result:
        print('检测出异常{}'.format(result))
    print('test3-2')
test3()
print('-------------')
test2()
'''
'''
import os,sys
temp=os.open('E:/vscodelearn/tmp/runoob26.txt',os.O_RDWR|os.O_CREAT)
temp_file=os.fdopen(temp,'r')
print(str(temp_file.read()))
os.close(temp)
'''
'''
with open('E:/vscodelearn/tmp/runoob27.txt','r') as f:
    print(f.read())
'''
'''
def model_exception(x,y):
    try:
        b=Name
        a=x/y
    except(ZeroDivisionError,NameError,TypeError):
        print('one of ZeroDivisionError or NameError or TypeError happend')
model_exception(2,0)
'''
'''
class MyClass:
    i=12345
    def f(self):
        return 'hello world'
x=MyClass()
print("MyClass类的属性i为:",x.i)
print("MyClass类的方法f输出为:",x.f())
'''
'''
class Complex:
    def __init__(self,realpart,imagpart):
        self.r=realpart
        self.i=imagpart
x=Complex(3.0,-4.5)
print(x.r,x.i)
'''
'''
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
t=Test()
t.prt()
'''
'''
class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
t=Test()
t.prt()
'''
'''
class people:
    name=''
    age=0
    _weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("%s说:我%d岁。"%(self.name,self.age))
p=people('runoob',10,30)
p.speak()
'''
'''
class people:
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("%s说:我%d岁。"%(self.name,self.age))
p=people('runoob',10,30)
p.speak()
'''
'''
class people:
    name=''
    age=0
    _weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self._weight=w
    def speak(self):
        print("%s说:我%d岁。"%(self.name,self.age))
class student(people):
    grade=''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade=g
    def speak(self):
        print("%s说:我%d岁了,我在读%d年级"%(self.name,self.age,self.grade))
s=student('ken',10,60,3)
s.speak()
'''
'''
class people:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return('这个人的名字是%s,已经有%d岁了!'%(self.name,self.age))
a=people('孙悟空',999)
print(a)
'''
'''
class Classname:
    @staticmethod
    def fun():
        print('静态方法')
    @classmethod
    def a(cls):
        print('类方法')
    #普通方法
    def b(self):
        print('普通方法')
Classname.fun()
Classname.a()
C=Classname()
C.fun()
C.a()
C.b()
'''
'''
class Classname:
    @staticmethod
    def fun():
        print('静态方法')
    @classmethod
    def a(cls):
        print('类方法')
    def b(self):
        print('普通方法')
Classname.fun()
Classname.a()
C=Classname()
C.fun()
C.a()
C.b()
'''
'''
class People:
    name=''
    age=0
    __weight=0
    def __init__(self,n,a,w):
        self.name=n
        self.age=a
        self.__weight=w
    def speak(self):
        print("%s say : i am %d."%(self.name,self.age))
p=People('Python',10,20)
p.speak()
print(p.name,'--',p.age)#,'--',p.__weight)
'''
'''
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return('Vector (%d,%d)'%(self.b,self.a))
    def __str__(self):
        return('Vector (%d,%d)'%(self.a,self.b))
    def __add__(self,other):
        return('Vector(self.a+other.a,self.b+other.b)')
v1=Vector(2,10)
print(v1)
'''
'''
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return('Vector (%d,%d)'%(self.b,self.a))
    def __str__(self):
        return('Vector (%d,%d)'%(self.a,self.b))
    def __add__(self,other):
        return('Vector(self.a+other.a,self.b+other.b)')
print(v1.__repr__())
'''
'''
class Test(object):
    def InstanceFun(self):
        print("InstanceFun");
        print(self);
    @classmethod
    def ClassFun(cls):
        print("ClassFun");
        print(cls);
    @staticmethod
    def StaticFun():
        print("StaticFun");
t=Test();
t.InstanceFun();
Test.ClassFun();
Test.StaticFun();
t.StaticFun();
t.ClassFun();
'''
'''
a=Myvector([1,2,3])
'''
'''
from numpy import *
l=zeros((5,4))#构建一个5*4的零矩阵
for i in range(5):#给该矩阵赋值
    for j in range(4):
        l[i][j]=i*5+j
print(l)#打印赋值后的矩阵
print(shape(l))#输出l的行列值
print(l.shape[0])#输出l的行数值
print(l.shape[1])#输出l的列数值
'''
