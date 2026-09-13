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
"""🐔#函数的参数
 #位置参数 在调用函数时通常按照从左到右的顺序依次传入，而且传入参数的数量必须和定义函数时参数的数量相同
def make_judgement(a, b, c):
    #判断三条边的长度能否构成三角形
    return a + b > c and b + c > a and a + c > b
print(make_judgement(1, 2, 3))  # False
print(make_judgement(4, 5, 6))  # True
   #如果不想按照从左到右的顺序依次给出a、b、c 三个参数的值，也可以使用关键字参数，通过“参数名=参数值”的形式为函数传入参数
print(make_judgement(b=2, c=3, a=1))  # False
print(make_judgement(c=6, b=4, a=5))  # True🐔"""

"""🐔  #/前面的参数是强制位置参数  调用函数时只能按照参数位置来接收参数值的参数
def make_judgement(a, b, c, /):
  #判断三条边的长度能否构成三角形
  return a + b > c and b + c > a and a + c > b🐔"""
"""
下面的代码会产生TypeError错误，错误信息提示“强制位置参数是不允许给出参数名的”
TypeError: make_judgement() got some positional-only arguments passed as keyword arguments
print(make_judgement(b=2, c=3, a=1))
"""
"""🐔  #*后面的参数是命名关键字参数  命名关键字参数只能通过“参数名=参数值”的方式来传递和接收参数
def make__judgement(*, a, b, c):
  #判断三条边的长度能否构成三角形
  return a + b > c and b + c > a and a + c > b🐔"""

"""
# 下面的代码会产生TypeError错误，错误信息提示“函数没有位置参数但却给了3个位置参数”
# TypeError: make__judgement() takes 0 positional arguments but 3 were given
# print(make__judgement(1, 2, 3))
"""
"""🐔 #参数的默认值
def add(a=0, b=0, c=0):
    #三个数相加求和
    return a + b + c
# 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add())         # 0
# 调用add函数，传入一个参数，该参数赋值给变量a, 变量b和c使用默认值0
print(add(1))        # 1
# 调用add函数，传入两个参数，分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2))     # 3
# 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(1, 2, 3))  # 6🐔"""
 #可变参数
"""
用星号表达式来表示args可以接收0个或任意多个参数
调用函数时传入的n个参数会组装成一个n元组赋给args
如果一个参数都没有传入，那么args会是一个空元组
"""
"""🐔def add(*args):
    total = 0
    #对保存可变参数的元组进行循环遍历
    for val in args:
        #对参数进行了类型检查（数值型的才能求和）
        if type(val) in (int, float):
            total += val
    return total
  #在调用add函数时可以传入0个或任意多个参数
print(add())         # 0
print(add(1))        # 1
print(add(1, 2, 3))  # 6
print(add(1, 2, 'hello', 3.45, 6))  # 12.45
print(add(int(input('a = ')), int(input('b = ')), int(input('c = '))))
  #对于最后一行代码，如果想要传输任意数量的数据到add函数中，则应改为如下代码
  #先把输入的所有数字收集到一个列表里，再用*解包传给add。
nums = input('请输入多个数，用空格分隔: ').split()  #字符串的split方法可以把字符串拆分成列表
print(add(*[float(x) for x in nums]))🐔"""
 #可变关键字参数
"""
参数列表中的**kwargs可以接收0个或任意多个关键字参数
调用函数时传入的关键字参数会组装成一个字典（参数名是字典中的键，参数值是字典中的值）
如果一个关键字参数都没有传入，那么kwargs会是一个空字典
"""
"""🐔def foo(*args, **kwargs):
    print(args)
    print(kwargs)
foo(3, 2.1, True, name='立源', age=19, GPA=3.89)🐔"""

#用模块管理函数
"""
Python中每个文件就代表了一个模块（module），我们在不同的模块中可以有同名的函数，
在使用函数的时候，我们通过import关键字导入指定的模块再使用完全限定名（模块名.函数名）的调用方式，就可以区分到底要使用的是哪个模块中的该同名函数
"""
"""🐔import Hello_World
import Structure
 #用“模块名.函数名”的方式（完全限定名）调用函数，
Hello_World.philia093()  #记忆的涟漪，等待被流星的亲吻唤醒，要用爱铭记我
Structure.philia093()  #以爱为一，涤荡憎恨。以我为一，改写毁灭
  #在导入模块时，还可以使用as关键字对模块进行别名，这样我们可以使用更为简短的完全限定名
import Hello_World as p1
import Structure as p2

p1.philia093()
p2.philia093()
 #如果我们从两个不同的模块中导入了同名的函数，后面导入的函数会替换掉之前的导入。若想解决此问题，可用as给函数加别名来区分
from Hello_World import philia093
from Structure import philia093

philia093()  #With love as one, cleanse hatred. With me as one, rewrite destruction.🐔"""

#标准库中的模块和函数
"""
Python 标准库中还有一类函数是不需要import就能够直接使用的，我们将其称之为内置函数，这些内置函数不仅有用而且还很常用，下面的表格列出了一部分的内置函数。
函数                              	说明
abs         	返回一个数的绝对值，例如：abs(-1.3)会返回1.3。
bin         	把一个整数转换成以'0b'开头的二进制字符串，例如：bin(123)会返回'0b1111011'。
chr         	将Unicode编码转换成对应的字符，例如：chr(8364)会返回'€'。
hex         	将一个整数转换成以'0x'开头的十六进制字符串，例如：hex(123)会返回'0x7b'。
input        	从输入中读取一行，返回读到的字符串。
len         	获取字符串、列表等的长度。
max         	返回多个参数或一个可迭代对象中的最大值，例如：max(12, 95, 37)会返回95。
min          	返回多个参数或一个可迭代对象中的最小值，例如：min(12, 95, 37)会返回12。
oct         	把一个整数转换成以'0o'开头的八进制字符串，例如：oct(123)会返回'0o173'。
open         	打开一个文件并返回文件对象。
ord         	将字符转换成对应的Unicode编码，例如：ord('€')会返回8364。
pow           	求幂运算，例如：pow(2, 3)会返回8；pow(2, 0.5)会返回1.4142135623730951。
print          	打印输出。
range          	构造一个范围序列，例如：range(100)会产生0到99的整数序列。
round          	按照指定的精度对数值进行四舍五入，例如：round(1.23456, 4)会返回1.2346。
sum         	对一个序列中的项从左到右进行求和运算，例如：sum(range(1, 101))会返回5050。
type        	返回对象的类型，例如：type(10)会返回int；而 type('hello')会返回str。
"""

#函数的应用
import random
import string

ALL_CHARS = string.digits + string.ascii_letters #string模块的digits代表0到9的数字构成的字符串，ascii_letters代表大小写英文字母构成的字符串
def generate_code(*, code_len=4):
    """
    生成指定长度的验证码
    :param code_len: 验证码的长度(默认4个字符)
    :return: 由大小写英文字母和数字构成的随机验证码字符串
    random模块的sample和choices函数都可以实现随机抽样，
    sample实现无放回抽样，这意味着抽样取出的元素是不重复的；choices实现有放回抽样，这意味着可能会重复选中某些元素。
    这两个函数的第一个参数代表抽样的总体，而参数k代表样本容量，
    需要说明的是choices函数的参数k是一个命名关键字参数，在传参时必须指定参数名。
    """
    return ''.join(random.choices(ALL_CHARS, k=code_len))
for _ in range(5):
    print(generate_code(code_len=6))













