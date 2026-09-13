"""🐔#定义函数
 #自定义阶乘函数
def fac(num): #用def关键字定义一个函数 def后接函数名，括号里为自变量（参数），return后为因变量（返回值）
    if num <= 1:
        return 1
    return num * fac(num - 1) #如果一个函数体内部没写return的内容，则该函数只会返回None
m = int(input('m = '))
n = int(input('n = '))
print(fac(m)//fac(n)//fac(m-n))
 #调用math模块里的factorial阶乘函数
import math  #或者使用from math import factorial来引入函数
m = int(input('m = '))
n = int(input('n = '))
print(math.factorial(m)//math.factorial(n)//math.factorial(m-n))
 #使用as关键字改写函数名
from math import factorial as f
m = int(input('m = '))
n = int(input('n = '))
print(f(m)//f(n)//f(m - n))🐔"""
#函数的参数
 #位置参数 在调用函数时通常按照从左到右的顺序依次传入，而且传入参数的数量必须和定义函数时参数的数量相同
def make_judgement(a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True
   #如果不想按照从左到右的顺序依次给出a、b、c 三个参数的值，也可以使用关键字参数，通过“参数名=参数值”的形式为函数传入参数
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True

  #/前面的参数是强制位置参数  调用函数时只能按照参数位置来接收参数值的参数
def make_judgement(a, b, c, /):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
"""
下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
print(make_judgement(b=2, c=3, a=1))
"""
  #*后面的参数是命名关键字参数  命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数
def make__judgement(*, a, b, c):
    """判断三条边的长度能否构成三角形"""
    return a + b > c and b + c > a and a + c > b
"""
# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make__judgement() takes 0 positional arguments but 3 were given
# print(make__judgement(1, 2, 3))
"""
 #参数的默认值
def add(a=0, b=0, c=0):
    """三个数相加求和"""
    return a + b + c
# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6




























