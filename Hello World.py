"""
这是我系统性学习Python的The First Day
希望疑虑的阴云能随着学习的深入而逐渐消散，冥茫也能荡然无存
"""

#昔涟.是桃子。是爱。
#昔涟。不喜欢眼泪。嘻嘻哈哈。
#昔涟是。温柔。爱美。会写诗。
#昔涟是。长不高的。会说话的。随风逝去后。仍被留下的。
#昔涟是。每一句最后的。一直咯咯笑的。像是小尾巴的。
#昔涟是。哭着诞生的。脆弱的。透明的。像是水晶的。
#昔涟是。笑着道别的。柔软的。粉色的。像是花的。
print("Hello World")
print("Philia093:See you tomorrow...")

"""🐔#二进制、八进制、十进制、十六进制
print(0b101,0o203,201,0x204)

#运算符
a = 100;b = 2;c=315
print(a**b)#10000
a*=b;b*=a+9
print(a,b,a:=c)#200 418 315  :=被称为海象运算符，解决了print等语句里面不能放赋值表达式的问题

#将华氏温度转换为摄氏温度（格式化处理）
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print(f'{f:.2f}华氏度={c:.2f}摄氏度')🐔"""
"""
字符串前面的f表示这个字符串是需要格式化处理的(即format)，
其中的{f:.2f}和{c:.2f}可以先看成是{f}和{c}，
表示输出时会用变量f和变量c的值替换掉这两个占位符，
后面的:.2f表示这是一个浮点数，小数点后保留2位有效数字
"""
"""🐔print(f'{int(f):d}F*={int(c):d}C*')🐔"""
"""
同理，:d表示这个将被替代的数是一个整型，此时需要做强制类型转换，否则会报错
因为最开始变量f被类型转换成了浮点型的，由浮点型f运算得到的c也是浮点型的
如果无需注重数据类型而只是单纯想格式化处理，则可如此书写：print(f'{f}F*={c}C*')
另外还有一种比较老的格式化处理的语句，例如：print('%.1f华氏度 = %.1f摄氏度' % (f, c))
这时占位符为%.1f，这两个占位符会被%之后的(f, c)中的两个float类型的变量值给替换掉
"""
"""🐔#输入半径计算圆的周长和面积
import math #导入math模块以使用其中的pi常量。
radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius#可以理解为C++中与类同名的类类型变量math去访问math类中的公有成员pi
area = math.pi * radius ** 2
print(f'周长: {perimeter:.2f}')
print(f'面积: {area:.2f}')🐔"""
"""
再引入一种最新的格式化处理语句：
print(f'{perimeter = :.2f}')  # 输出：perimeter = 34.56
print(f'{area = :.2f}')       # 输出：area = 95.03
假如变量a的值是9.87，那么字符串f'{a = }'的值是a = 9.87；而字符串f'{a = :.1f}'的值是a = 9.9。
这种格式化输出的方式会同时输出变量名和变量值。
"""

"""🐔#if-else 结构 BMI计算器
height = float(input('身高(cm)：'))
weight = float(input('体重(kg)：'))
bmi = weight / (height / 100) ** 2
print(f'{bmi = :.1f}')
if bmi < 18.5:
    print('你的体重过轻！')
elif bmi < 24:
    print('你的身材很棒！')
elif bmi < 27:
    print('你的体重过重！')
elif bmi < 30:
    print('你已轻度肥胖！')
elif bmi < 35:
    print('你已中度肥胖！')
else:
    print('你已重度肥胖！') #良子166.5cm，171.5kg🐔"""

"""🐔#match-case 结构 HTTP 响应状态码识别  相当于C++中的switch-case
status_code = int(input('响应状态码: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)
print(f'状态码描述：{description:.3s}')🐔"""
"""
带有_的case语句在代码中起到通配符的作用，如果前面的分支都没有匹配上，代码就会来到case _
case _的是可选的，并非每种分支结构都要给出通配符选项。
如果分支中出现了case _，它只能放在分支结构的最后面，如果它的后面还有其他的分支，那么这些分支将是不可达的。
这相当于C++中的default语句 
"""
"""🐔status_code = int(input('响应状态码: '))#另外，match-case语句还有如下一种合并模式的表达形式
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('状态码描述:', description)#也可写成print(f'状态码描述：{description}')🐔"""

"""🐔#for-in循环 求0到100偶数和
total=0
for i in range(0,101,2):
    total += i
print(total)
#更为简单的办法是使用 Python 内置的sum函数求和，这样我们连循环结构都省掉了。
# 即print(sum(range(0 101, 2)))🐔"""

"""🐔#while循环 求0到1000奇数和
total = 0
i = 1
while i <= 1000:
    total += i
    i += 2
print(total)🐔"""

"""
对于break和continue关键字，这边直接口头叙述其在循环语句块中起到的作用：
break关键字，它的作用是终止循环结构的执行。需要注意的是，break只能终止它所在的那个循环，这在嵌套循环中尤其注意
continue关键字，它可以用来放弃本次循环后续的代码直接让循环进入下一轮，时常与if语句同时使用
比如
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)
continue的存在会使该循环跳过i为奇数的情况，即i为奇数时不执行continue后续语句，
而是直接进入下一个循环，再让新的i值去进行if语句判定，判定为False才能执行循环体中的后续语句
简单来讲，
break：一旦执行，整个循环立即结束，程序跳出循环，执行循环后面的代码。
continue：一旦执行，本次循环的剩余代码全部跳过，直接进入下一次循环的判断条件。
"""
"""🐔#嵌套的循环结构 打印九九乘法表
#固定外层，进入内层循环，一次内层循环结束后回到外层递归，外层产生一个新的值后固定此值再进入内层继续完整循环一次
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i}×{j}={i * j}', end='\t')#print完后添加的是制表符\t而不是默认的换行符\n
    print()#用于换行，就算括号里面什么都不写也默认有一个换行符\n🐔"""

"""🐔#常用的平方数
counter=3
for i in range(1, 21):
    for j in range(1, i+1):
        if i==j:
            counter+=1
            if counter%4==0:
                print()
            print(f'{i}*{j}={i * j}', end='\t')
print()🐔"""

"""🐔#判断是否为素数
n=int(input('请输入一个大于1的正整数：'))
is_prime=True
for i in range(2,int(n**0.5)+1):#range中的参数必须是整型，必要时可做强制类型转换
    if n % i == 0:#如果2到根号n中存在n的因数，则n不是素数，这是判断的基本原理
        is_prime=False
        break#加快程序响应速度
if is_prime:
    print(f'{n}是素数')
else:
    print(f'{n}不是素数')🐔"""

"""🐔#求两个数的最大公因数 常规解法
xn=int(input('x='));x=xn#这里只是为了后面的格式化输出时使用变量x所以才引入一个xn来代替x放进循环体
y=int(input('y='))
for i in range(xn,0,-1):
    if xn % i == 0 and y % i == 0:
        print(f'{x}和{y}的最大公约数为{i}')
        break

#求最大公因数 欧几里得算法
x = int(input('x = '))
y = int(input('y = '))
while y % x != 0:
    x, y = y % x, x
print(f'最大公约数: {x}')🐔"""

"""🐔import random
answer = random.randrange(1, 101)#生成一个1到100的随机数并赋值给answer
counter = 0#计数器初始化值
while True:
    counter += 1
    num = int(input('请输入: '))
    if num < answer:
        print('你归骰叔叔的ρ蚌更大.')
    elif num > answer:
        print('吓死你归骰外公了.')
    else:
        print('猜对啦我的宝贝星核精.')
        break
print(f'你一共猜了{counter}次。')
if counter>5:
    print("愿此行，终抵毁灭尽头")
else:
    print("本归骰允许你用星核放歌")🐔"""

"""🐔#输出0到100的所有素数
import math
counter=0
for num in range(2,201):
    is_prime=True
    for i in range(2,math.isqrt(num)+1):
#sqrt()就是取平方，但输出的数值是浮点型，要么进行强制类型转换，要么直接用isqrt()输出整型
        if num % i == 0:
            is_prime=False
            break#只要有除1以外的因数就不是素数，直接跳出整个内循环然后回到外循环继续
    if is_prime:
         print(f'{num}',end='\t')
         counter+=1
#在循环体外引入计数器counter，若counter累加到6时便执行换行语句，使得生成结果每六个数就排成一行
         if counter%6==0:
             print()🐔"""

"""🐔#斐波那契数列 Python实现这个的语句块看起来比C++简单太多了....
a=0;b=1;counter=0
for i in range(1,21):
    a,b=b,a+b#表示把b的值赋给a，把a+b的值赋给b。Python这比较随意，没有C++那么格式化
    print(a,end='\t')
    counter+=1
    if counter%4==0:
        print()#只是为了排版好看🐔"""

"""🐔#正整数的反转 挺常用的这个拆分数的方法
num = int(input('num = '))
reversed_num = 0
while num > 0:
    reversed_num = reversed_num * 10 + num % 10
    num //= 10
print(reversed_num)
#比如输入个12389进去，在循环体内r_n先变成9，然后n变成1238;再次循环，r_n变为98，n变为123,...🐔"""

"""🐔#百钱百鸡问题
for x in range(1,21):
    for y in range(1,34):
        if (100-x-y)%3==0 and x*5+y*3+(100-x-y)//3==100:
            print(f'公鸡有{x}只，母鸡有{y}只，小鸡有{100-x-y}只')🐔"""

"""🐔#Craps赌博游戏
import random
import time

money = 2000
while money > 0:
    print(f'你的总资产为: {money}千万元。')
    # 下注金额必须大于0且小于等于玩家的总资产
    while True:
        debt = int(input('请下注: '))
        if 0 < debt <= money:
            break
    # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
    first_point = random.randrange(1, 7) + random.randrange(1, 7)
    print(f'\n星核精摇出了{first_point}点')
    if first_point == 7 or first_point == 11:
        print('星核精胜!\n')
        money += debt
    elif first_point == 2 or first_point == 3 or first_point == 12:
        print('大禽胜!\n')
        money -= debt
    else:
        # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
        while True:
            current_point = random.randrange(1, 7) + random.randrange(1, 7)
            print(f'星核精摇出了{current_point}点')
            if current_point == 7:
                print('大禽胜!\n')
                money -= debt
                break
            elif current_point == first_point:
                print('星核精胜!\n')
                money += debt
                break
messages=['你破产了，按照“不要钱挑战”合同约定，星穹列车欠大禽200亿元。',
      '姬子：星核精，你可算来了，咱们列车已经揭不开锅了。',
      '姬子：不，准确来说已经没有列车了。公司说列车是上个琥珀纪的遗物，能源利用效率太低，不符合现在的星际环保标准，罚了我们好大一笔钱。',
      '姬子·骑行：我们的列车已经被强制征收拆解，回收材料用于制造新一代的星际单人独轮车了。',
      '丹恒：你的冠军奖杯，智库的收藏，杨叔的模型，列车长的零食箱、还有列车长也全被没收了',
      '星期日：我听说列车长要被送进动物园里，以后只能买票看它了。',
      '瓦尔特：那就是永别了。毕竟，我们哪儿有买票的钱啊......',
      '姬子·骑行：艾丝妲小姐给我们找了份工，只要我们一家人齐心工作，8000年就能还上了。',
      '三月七：...8000年？我从今天开始就戒奶茶，能省一点是一点。']
for msg in messages:
    print(msg)
    time.sleep(3)🐔"""

"""🐔#创建与输出列表
items1 = [35, 12, 99, 68, 55, 35, 87]
items2 = ['Python', 'Java', 'Go', 'Kotlin']
items3 = [100, 12.3, 'Python', True]
items4 = list(range(1, 10))
items5 = list('hello')
print(items1)  # [35, 12, 99, 68, 55, 35, 87]
print(items2)  # ['Python', 'Java', 'Go', 'Kotlin']
print(items3)  # [100, 12.3, 'Python', True]
print(items4)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(items5)  # ['h', 'e', 'l', 'l', 'o']
print(type(items3))🐔"""

"""🐔#列表的运算
items5 = [35, 12, 99, 45, 66]
items6 = [45, 58, 29]
items7 = ['Python', 'Java', 'JavaScript']
   #使用+运算符实现两个列表的拼接，拼接运算会将两个列表中的元素连接起来放到一个列表中
print(items5 + items6)  # [35, 12, 99, 45, 66, 45, 58, 29]
print(items6 + items7)  # [45, 58, 29, 'Python', 'Java', 'JavaScript']
items5 += items6
print(items5)  # [35, 12, 99, 45, 66, 45, 58, 29]
   #使用*运算符实现列表的重复运算，*运算符会将列表元素重复指定的次数
print(items6 * 3)  # [45, 58, 29, 45, 58, 29, 45, 58, 29]
print(items7 * 2)  # ['Python', 'Java', 'JavaScript', 'Python', 'Java', 'JavaScript']
   #使用in或not in运算符判断一个元素在不在列表中
print(29 in items6)  # True
print(99 in items6)  # False
print('C++' not in items7)     # True
print('Python' not in items7)  # False🐔"""

"""
当我们想操作列表中的某个元素时，可以使用[]字面量运算符，通过在[]中指定元素的位置来访问该元素，这种运算称为索引运算。
需要说明的是，[]的元素位置可以是0到N-1的整数，也可以是-1到-N的整数，分别称为正向索引和反向索引，其中N代表列表元素的个数。
对于正向索引，[0]可以访问列表中的第一个元素，[N-1]可以访问最后一个元素；
对于反向索引，[-1]可以访问列表中的最后一个元素，[-N]可以访问第一个元素
"""
"""🐔#访问与操作列表中的元素
items8 = ['apple', 'waxberry', 'pitaya', 'peach', 'watermelon']
print(items8[0])   # apple
print(items8[2])   # pitaya
print(items8[4])   # watermelon
items8[2] = 'durian' #将索引值为2的元素替换成’durian‘
print(items8)      # ['apple', 'waxberry', 'durian', 'peach', 'watermelon']
print(items8[-5])  # 'apple'
print(items8[-4])  # 'waxberry'
print(items8[-1])  # watermelon
items8[-4] = 'strawberry'
print(items8)      # ['apple', 'strawberry', 'durian', 'peach', 'watermelon']🐔"""

"""
如果希望一次性访问列表中的多个元素，我们可以使用切片运算。切片运算是形如[start:end:stride]的运算符，
其中start代表访问列表元素的起始位置，end代表访问列表元素的终止位置（终止位置的元素无法访问），
而stride则代表了跨度，简单的说就是位置的增量，且当跨度值为默认的1时，这个1甚至其前的:都可以省略不写
比如我们访问的第一个元素在start位置，那么第二个元素就在start + stride位置，当然start + stride要小于end
"""
"""🐔items8 =['apple', 'strawberry', 'durian', 'peach', 'watermelon']
print(items8[1:3:1])     # ['strawberry', 'durian']#如果stride值等于1，那么在使用切片运算符时可以将其省略。
print(items8[0:3:1])     # ['apple', 'strawberry', 'durian']#如果start值等于0，那么在使用切片运算符时可以将其省略；
print(items8[0:5:2])     # ['apple', 'durian', 'watermelon']#如果end值等于N或-N-1，N代表列表元素的个数，那么在使用切片运算符时可以将其省略；
print(items8[-4:-2:1])   # ['strawberry', 'durian']
print(items8[-2:-6:-1])  # ['peach', 'durian', 'strawberry', 'apple']
    #还可以通过切片操作修改列表中的元素
items8[1:3] = ['x', 'o']
print(items8)  # ['apple', 'x', 'o', 'peach', 'watermelon']🐔"""

"""🐔#元素的遍历 使用for-in循环
  #方法一：索引运算
languages = ['Python', 'Java', 'C++', 'Go']
for index in range(len(languages)):
    #len()用于返回一个容器内有多少个元素，比如此处len(languages)的值为4
    #至于range(4)，这会生成一个0到3的整数序列0,1,2,3（不包括4）
    print(languages[index])
    #当索引运算的对象是变量（比如这里的index）时，会依次取出列表中的每个元素
  #方法二：对列表做循环  方便得多
languages = ['Python', 'Java', 'C++', 'Go']
for language in languages:
    print(language)🐔"""

"""🐔  #Practice 当列表中元素个数不确定（即len(items)不确定）时
import random
length=random.randint(1,10)  #调用模块random中的函数randint可以生成一个给定闭区间的任意数值
items=list(random.randrange(1,100) for i in range(length))
for index in range(len(items)):
  print(items[index])
for item in items:
  print(item)🐔"""

"""🐔#列表的应用  掷色子统计每种点数出现次数
import random

counters = [0] * 6#创建一个[0,0,0,0,0,0]的列表。也可先创建再扩展，如counters = [0];counters *= 6
  #模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)#掷出骰子的面数是随机的
    counters[face - 1] += 1#索引=面数-1，比如掷出点数为5的面就需要用counters[4]来进行索引运算来修改对应面的投掷数据
  #输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')#用索引运算读取掷完6000次后的列表数据🐔"""

"""🐔#向列表中添加元素
languages = ['Python', 'Java', 'C++']
languages.append('JavaScript')#使用列表的append方法向列表中追加元素，追加指的是将元素添加到列表的末尾
print(languages)  # ['Python', 'Java', 'C++', 'JavaScript']
languages.insert(1, 'SQL')#使用insert方法向列表中插入元素，插入是在指定的位置添加新元素
print(languages)  # ['Python', 'SQL', 'Java', 'C++', 'JavaScript']🐔"""

"""🐔#删除列表中的元素
languages = ['Python', 'SQL', 'Java', 'C++', 'JavaScript']
  #用列表的remove方法从列表中删除指定元素。建议删除之前先用成员运算做一个该元素是否在列表中的判断，以免程序崩溃
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)  # ['Python', 'SQL', C++', 'JavaScript']
  #使用pop方法从列表中删除元素，pop方法默认删除列表中的最后一个元素，当然也可以给一个位置，删除指定位置的元素，但索引值不能超范围
languages.pop() #删除最后一个元素
print(languages) #['Python', 'SQL', 'C++']
temp = languages.pop(1) #删除索引为1的（列表中第二个）元素，并将这个元素赋给变量temp
print(languages)  #['Python', 'C++']
print(temp)       # SQL
languages.append(temp)
print(languages)  # ['Python', C++', 'SQL']
  #使用clear方法，可以清空列表中的元素
languages.clear()
print(languages)  # []
  #使用Python中的del关键字后面跟要删除的元素,实现的效果和pop一样但性能更优
items = ['Python', 'Java', 'C++']
del items[1]
print(items)  # ['Python', 'C++']🐔"""

"""🐔 #practice
items= ['th', 'Romin','yq','hxb','zyc','dxh']
print(items)
items.append('lx')
print(items)
items.insert(1,'ztq')
print(items)
items.remove('dxh')
print(items)
items.pop(3)
print(items)
del items[2]
print(items)
items.clear()
print(items)🐔"""

"""🐔#元素位置和频次
items = ['Python', 'Java', 'Java', 'C++', 'Kotlin', 'Python']
  #列表的index方法可以查找某个元素在列表中的索引位置,从左至右直到结束，不会掉头或是读取完一遍后又从第一个元素开始重新读直到找到该元素
print(items.index('Python'))     # 0
# 从索引位置1开始查找'Python'
print(items.index('Python', 1))  # 5
  #列表的count方法可以统计一个元素在列表中出现的次数
print(items.count('Python'))     # 2
print(items.count('Kotlin'))     # 1
print(items.count('Swift'))      # 0
# 从索引位置3开始查找'Java'
#print(items.index('Java', 3))    # ValueError: 'Java' is not in list🐔"""

"""🐔#元素排序与反转
items = ['Python', 'Java', 'C++', 'Kotlin', 'Swift']
items.sort() #列表的sort操作可以实现列表元素的排序 对于基础排序：数字按大小排，字符串按Unicode码表排，两者混合则无法排序
print(items)  # ['C++', 'Java', 'Kotlin', 'Python', 'Swift']
items.reverse() #reverse操作可以实现元素的反转
print(items)  # ['Swift', 'Python', 'Kotlin', 'Java', 'C++']🐔"""

#列表生成式  在 Python 中，列表还可以通过一种特殊的字面量语法来创建，这种语法叫做生成式
'''
列表生成式的基本结构为 [表达式 for 变量 in 可迭代对象 if 条件]
它等价于：
新列表 = []
for 变量 in 可迭代对象:
    if 条件:
        新列表.append(表达式)
'''
"""🐔 #场景一：创建一个取值范围在1到99且能被3或者5整除的数字构成的列表。
items = [i for i in range(1, 100) if i % 3 == 0 or i % 5 == 0]
print(items)
#场景二：有一个整数列表nums1，创建一个新的列表nums2，nums2中的元素是nums1中对应元素的平方。
nums1 = [35, 12, 97, 64, 55]
nums2 = [num ** 2 for num in nums1]
print(nums2)
#场景三： 有一个整数列表nums1，创建一个新的列表nums2，将nums1中大于50的元素放到nums2中。
nums1 = [35, 12, 97, 64, 55]
nums2 = [num for num in nums1 if num > 50]
print(nums2)
  #例如场景三 列表生成式是对如下较麻烦且吃算力的代码的简化
nums1 = [35, 12, 97, 64, 55]
nums2 = []
for num in nums1:
   if num > 50:
       nums2.append(num)
print(nums2)
items1=[random.randrange(1, 10) for i in range(1, 10)] #生成9个取值范围为1——10左开右闭区间的数
print(items1)
 #注：items=[任意有定义的元素]与items=list(与前者完全相同的元素)等价🐔"""

"""🐔#嵌套列表 即列表中的元素也为列表
 #使用嵌套列表存储与读取五名学生的三科成绩
scores = [[95, 83, 92], [80, 75, 82], [92, 97, 90], [80, 78, 69], [65, 66, 89]]
print(scores[0]) #使用一次索引运算 输出索引为0的元素，即列表 [95, 83, 92]
print(scores[0][1]) #使用两次索引运算 输出索引为0的列表里索引为1的元素 83
 #通过键盘输入来添加与存储上述成绩
scores = []
for _ in range(5):
   temp = []
   for _ in range(3):
       score = int(input('请输入: '))
       temp.append(score)
   scores.append(temp)
print(scores)
#通过列表生成式来产生嵌套列表（数据随机）
import random
scores = [[random.randrange(60, 101) for _ in range(3)] for _ in range(5)]
  #range(3)相当于在for循环中依次取0,1,2，循环执行3次。这在之前也有过解释
print(scores)🐔"""

"""🐔#双色球随机选号程序  国内各种形式的彩票的本质：虚构一个不劳而获的人，去忽悠一群想不劳而获的人，最终养活一批真正不劳而获的人
import random

n = int(input('生成几注号码: '))
red_balls = [i for i in range(1, 34)]
blue_balls = [i for i in range(1, 17)]
for _ in range(n):
    # 从红色球列表中随机抽出6个红色球（无放回抽样）
    selected_balls = random.sample(red_balls, 6) #利用random模块提供的sample函数来实现无放回随机抽样
    # 对选中的红色球排序
    selected_balls.sort()
    # 输出选中的红色球
    for ball in selected_balls:
        print(f'\033[031m{ball:0>2d}\033[0m', end=' ')
    # 从蓝色球列表中随机抽出1个蓝色球
    blue_ball = random.choice(blue_balls) #利用random模块提供的choice函数来实现随机抽取一个元素
    # 输出选中的蓝色球
    print(f'\033[034m{blue_ball:0>2d}\033[0m')
    #上面代码中print(f'\033[0m...\033[0m')是为了控制输出内容的颜色🐔"""
#Python 中的列表底层是一个可以动态扩容的数组，列表元素在计算机内存中是连续存储的，所以可以实现随机访问（通过一个有效的索引获取对应的元素且操作时间与列表元素个数无关）。

#元组的定义与运算
"""
元组也是多个元素按照一定顺序构成的序列,但元组是不可变类型，
这就意味着元组类型的变量一旦定义，其中的元素不能再添加或删除，而且元素的值也不能修改
就像列表可以用字面量[]来定义一般，定义元组通常使用形如(x, y, z)的字面量语法
也如同列表可以用list这个内置类型（类构造器）来创建一般，元组也可用tuple这个内置类型来创建
"""
"""🐔#下面是元组运算的一些实例，与列表的运算有很大的相似性
  #定义一个三元组
t1 = (35, 12, 98)
  #定义一个四元组
t2 = ('刘ly', 19, True, '四川自贡')
  #查看变量的类型
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'tuple'>
  #查看元组中元素的数量
print(len(t1))  # 3
print(len(t2))  # 4
  #索引运算
print(t1[0])    # 35
print(t1[2])    # 98
print(t2[-1])   # 四川自贡
  #切片运算
print(t2[:2:])   # ('刘ly', 19)
print(t2[::3])  # ('刘ly', '四川自贡')
  #循环遍历元组中的元素
for i in range(len(t1)):
    print(t1[i]) #若写成print(t1[i],end=' ')，元组中的数据将横向输出

for elem in t1:
    print(elem)
  #成员运算
print(12 in t1)         # True
print(99 in t1)         # False
if 'Felix Morrow' not in t2:
    print('True')# True
  #拼接运算
t3 = t1 + t2
print(t3)  # (35, 12, 98, '刘ly', 19, True, '四川自贡')
  #比较运算
print(t1 == t3)            # False
print(t1 >= t3)            # False
print(t1 <= (35, 11, 99))  # False🐔"""
'''
如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数
即便用item=tuple([random.randint(1, 10) for i in range(1, 2)])来产生一元组，
print(item)时输出结果也会自带逗号
'''

"""🐔#打包和解包操作
#当我们把多个用逗号分隔的值赋给一个变量时，多个值会打包成一个元组类型；当我们把一个元组赋值给多个变量时，元组会解包成多个值然后分别赋给对应的变量
  #打包操作
a = 1, 10, 100
print(type(a))  # <class 'tuple'>
print(a)        # (1, 10, 100)
  #解包操作 解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异常
i, j, k = a
print(i, j, k)  # 1 10 100
#通过星号表达式，我们可以让一个变量接收多个值，以解决变量个数少于元素的个数的情况，避免程序运行异常
#用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。并且，在解包语法中，星号表达式只能出现一次
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)        # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)        # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)        # [1, 10] 100 1000
*i, j = a
print(i, j)           # [1, 10, 100] 1000
i, *j = a
print(i, j)           # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)     # 1 10 100 [1000]
i, j, k, l,*m = a
print(i, j, k, l, m)  # 1 10 100 1000 []
#解包语法对所有的序列都成立，这就意味着列表、range函数构造的范围序列甚至字符串都可以使用解包语法
a, b, *c = range(1, 10)
print(a, b, c) #1 2 [3, 4, 5, 6, 7, 8, 9]
a, b, c = [1, 10, 100]
print(a, b, c) #1 10 100
a, *b, c = 'hello'
print(a, b, c) #h ['e', 'l', 'l'] o🐔"""

"""🐔#Python中的元组和列表类型是可以通过使用对应的类构造器相互转换的
items1 = ('刘ly', 19, True, '四川自贡')
print(list(items1))  # ['刘ly', 19, True, '四川自贡'] #将元组转换成列表
items2 = ['apple', 'banana', 'orange']
print(tuple(items2))  # ('apple', 'banana', 'orange') #将列表转换成元组🐔"""
'''
列表和元组都是容器型的数据类型，即一个变量可以保存多个数据，而且它们都是按一定顺序组织元素的有序容器。
列表是可变数据类型，元组是不可变数据类型，所以列表可以添加元素、删除元素、清空元素、排序反转，但这些操作对元组来说是不成立的。
列表和元组都可以支持拼接运算、成员运算、索引运算、切片运算等操作，
字符串类型也支持这些运算，因为字符串就是字符按一定顺序构成的序列
'''

#在 Python 程序中，我们把单个或多个字符用单引号或者双引号包围起来，就可以表示一个字符串
r'''
在字符串中使用\（反斜杠）来表示转义，也就是说\后面的字符不再是它原来的意义，
例如：\n不是代表字符\和字符n，而是表示换行；\t也不是代表字符\和字符t，而是表示制表符。
所以如果字符串本身又包含了'、"、\这些特殊的字符，必须要通过\进行转义处理
'''
r"""🐔#输出一个带单引号或反斜杠的字符串
s1 = '\'hello, world!\''
s2 = '\\hello, world!\\'
print(s1) #'hello, world!'
print(s2) #\hello, world!\🐔"""

"""
注：反斜杠不能通过 """ """ 注释掉，因为三引号不是注释，而是字符串。#才是注释，注释内的反斜杠不会有任何转义效果。
如果需要在字符串中保留反斜杠，使用 r"""  """ 原始字符串或双反斜杠。若不使用原始字符串，则双引号之间的反斜杠可能会对代码运行造成干扰
"""


r"""🐔#原始字符串 Python中的一种以r或R开头的字符串，意思是字符串中的每个字符都是它本来的含义，没有所谓的转义字符。
s1 = '\it \is \time \to \read \now'  #报错，且无法得到像s2的输出那样的结果
s2 = r'\it \is \time \to \read \now'  #\it \is \time \to \read \now
print(s1)
print(s2)🐔"""
#上面的变量s1中，\t、\r和\n都是转义字符。\t是制表符（table），\n是换行符（new line），\r是回车符（carriage return）相当于让输出回到了行首。

#字符的特殊表示
r"""
Python中还允许在\后面还可以跟一个八进制或者十六进制数来表示字符，
例如\141和\x61都代表小写字母a，前者是八进制的表示法，后者是十六进制的表示法。
另外一种表示字符的方式是在\u后面跟Unicode字符编码,例如'\u7acb\u6e90'代表的是中文“立源”
"""
r"""🐔s1 = '\141\142\143\x61\x62\x63'
s2 = '\u7acb\u6e90'
print(s1)
print(s2)🐔"""

#字符串的运算
'''
Python为字符串类型提供了非常丰富的运算符，有很多运算符跟列表类型的运算符作用类似
比如可以使用+运算符来实现字符串的拼接，可以使用*运算符来重复一个字符串的内容，
可以使用in和not in来判断一个字符串是否包含另外一个字符串，也可以用[]和[:]运算符从字符串取出某个字符或某些字符
'''
r"""🐔
  #拼接和重复
s1 = 'hello' + ', ' + 'world'
print(s1)    # hello, world
s2 = '!' * 3
print(s2)    # !!!
s1 += s2
print(s1)    # hello, world!!!
s1 *= 2
print(s1)    # hello, world!!!hello, world!!!
print('a'*10)  #aaaaaaaaaa🐔"""

  #比较运算
"""
对于两个字符串类型的变量，可以直接使用比较运算符来判断两个字符串的相等性或比较大小。
需要说明的是，因为字符串在计算机内存中也是以二进制形式存在的，那么字符串的大小比较比的是每个字符对应的Unicode码点的大小
字符串比较和查英文词典类似：从左到右，一个字符一个字符比较；如果当前字符相同，就继续比较下一个字符；
如果不清楚两个字符对应的码点到底是多少，可以使用ord()函数来获得
"""
r"""🐔
s1 = 'a whole new world'
s2 = 'hello world'
print(s1 == s2)             # False
print(s1 < s2)              # True 因为a的编码小于h，后面的就都不用比较了，直接判定s1<s2成立
print(s1 == 'hello world')  # False
print(s2 == 'hello world')  # True
print(s2 != 'Hello world')  # True
s3 = '立源'
print(ord('立'))            # 31435
print(ord('源'))            # 28304
s4 = '枫陌'
print(ord('枫'))            # 26539
print(ord('陌'))            # 38476
print(s3 >= s4)             # True
print(s3 != s4)             # True🐔"""

r"""🐔  #成员运算
s1 = 'hello, world'
s2 = 'goodbye, world'
print('wo' in s1)      # True
print('db' not in s2)  # False
print(s2 in s1)        # False🐔"""

r"""🐔   #索引运算和切片运算 运算逻辑和列表、元组没区别，但字符串是不可变类型，所以不能通过索引运算修改字符串中的字符
s = 'abc123456'
n = len(s)
print(s[0], s[-n])    # a a
print(s[n-1], s[-1])  # 6 6
print(s[2], s[-7])    # c c
print(s[5], s[-4])    # 3 3
print(s[2:5])         # c12
print(s[-7:-4])       # c12
print(s[2:])          # c123456
print(s[:2])          # ab
print(s[::2])         # ac246
print(s[::-1])        # 654321cba🐔"""

"""🐔#字符串的遍历 与列表、元组一样，也可用for循环的两种形式来遍历输出
  #方式一
s ='hello'
for i in range(len(s)):
  print(s[i])
  #方式二
s = 'hello'
for elem in s:
    print(elem)🐔"""

#字符串的方法
"""🐔 #大小写相关操作
s1 = 'hello, world!'
 #字符串首字母大写
print(s1.capitalize())  # Hello, world!
 #字符串每个单词首字母大写
print(s1.title())       # Hello, World!
 #字符串变大写
print(s1.upper())       # HELLO, WORLD!
s2 = 'GOODBYE'
 #字符串变小写
print(s2.lower())       # goodbye
 #检查s1和s2的值
print(s1)               # hello, world
print(s2)               # GOODBYE🐔"""
'''
正如前面我们所说，字符串是不可变类型，故当使用字符串的方法时，
并不像使用列表的方法一样对原列表进行改动，而是直接产生新的字符串。而原来的字符串不会受到任何影响
'''

 #查找操作
'''
如果想在一个字符串中从前向后查找有没有另外一个字符串，可以使用字符串的find或index方法。
在使用find和index方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为0的位置开始。
find方法找不到指定的字符串会返回-1，index方法找不到指定的字符串会引发ValueError错误。
'''
"""🐔  #正向查找，使用find或index
s = 'hello,world!'
print(s.find('or'))      # 7 索引位置为7，直接数的话在第8位，因为字符串的索引位置也是从0开始计数的
print(s.find('or', 9))   # -1
print(s.find('of'))      # -1
print(s.index('or'))     # 7
print(s.index('or', 9))  # ValueError: substring not found
#若需要逆向查找（从后向前查找），则可使用rfind或rindex
s = 'hello world!'
print(s.find('o'))       # 4
print(s.rfind('o'))      # 7
print(s.rindex('o'))     # 7
print(s.rindex('o', 8))  # ValueError: substring not found🐔"""

"""🐔 #性质判断
#可以通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾；还可以用is开头的方法判断字符串的特征，这些方法都返回布尔值
s1 = 'hello, world!'
print(s1.startswith('He'))   # False
print(s1.startswith('hel'))  # True
print(s1.endswith('!'))      # True
s2 = 'abc123456'
print(s2.isdigit())  # False isdigit用来判断字符串是不是完全由数字构成的
print(s2.isalpha())  # False isalpha用来判断字符串是不是完全由除Emoji外的Unicode字符构成的
print(s2.isalnum())  # True  isalnum用来判断字符串是不是由字母和数字构成的🐔"""

"""🐔 #格式化
#在Python中，字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。如果要在字符串的左侧补零，也可以使用zfill方法。
s = 'hello, world'
print(s.center(20, '*'))  #****hello, world****  总宽度为20，字符串s居中且占12个宽度，其余部分用*填充
print(s.rjust(20))        #        hello, world  总宽度为20，s右对齐，占8个宽度的其余部分用空格填充
print(s.ljust(20, '~'))   #hello, world~~~~~~~~ 原理同上
print('33'.zfill(5))      #00033  zfill的意思是“zero fill”，用0在左边填充，直到字符串达到设定的总宽度值，比如这里是5
print('-33'.zfill(5))     #-0033
print('+33'.zfill(5))     #+0033
#在用print函数输出字符串时，可以在字符串前加上f来格式化字符串，在这种以f打头的字符串中，{变量名}是一个占位符，会被变量对应的值将其替换掉
a = 321
b = 123
print(f'{a} * {b} = {a * b}')🐔"""
"""
如果需要进一步控制格式化语法中变量值的形式，可以参照下面的表格来进行字符串格式化操作。
变量值	    占位符	    格式化结果	        说明
3.1415926	{:.2f}  	'3.14'      	保留小数点后两位
3.1415926	{:+.2f}	    '+3.14'     	带符号保留小数点后两位
-1          {:+.2f}	    '-1.00'     	带符号保留小数点后两位
3.1415926	{:.0f}  	'3'         	不带小数
123	        {:0>10d}	'0000000123'	左边补0，补够10位
123	        {:x<10d}	'123xxxxxxx'	右边补x ，补够10位
123      	{:>10d} 	'       123'	左边补空格，补够10位
123     	{:<10d} 	'123       '	右边补空格，补够10位
123456789	{:,}	    '123,456,789'	逗号分隔格式
0.123   	{:.2%}  	'12.30%'    	百分比格式
123456789	{:.2e}  	'1.23e+08'  	科学计数法格式
"""

 #修剪操作
"""
字符串的strip方法可以帮我们获得将原字符串修剪掉左右两端指定字符之后的字符串，默认是修剪空格字符。
这个方法非常有实用价值，可以用来将用户输入时不小心键入的头尾空格等去掉，
strip方法还有lstrip和rstrip两个版本,分别用于左修剪和右修剪
"""
"""🐔s1 = '   fengmox949@gmail.com  '
print(s1.strip())      #fengmox949@gmail.com
s2 = '~你好，世界~'
print(s2.lstrip('~'))  #你好，世界~
print(s2.rstrip('~'))  #~你好，世界🐔"""

 #替换操作
"""
如果希望用新的内容替换字符串中指定的内容，可以使用replace方法。
replace方法的第一个参数是被替换的内容，第二个参数是替换后的内容，还可以通过第三个参数指定替换的次数。
"""
"""🐔s = 'hello, good world'
print(s.replace('o', '@'))     # hell@, g@@d w@rld
print(s.replace('o', '@', 2))  # hell@, g@od world🐔"""

"""🐔 #拆分与合并
 #可以使用字符串的split方法将一个字符串拆分为多个字符串（放在一个列表中），也可以使用字符串的join方法将列表中的多个字符串连接成一个字符串
s = 'See you tomorrow'
words = s.split()  
print(words)            #['See', 'you', 'tomorrow']  split默认按空白字符（空格、换行、制表符等）拆分字符串，返回一个列表。
print('~'.join(words))  #See~you~tomorrow  join 是字符串的方法，调用它的字符串就是分隔符。
 #split方法默认使用空格进行拆分，也可以指定其他的字符来拆分字符串，而且还可以指定最大拆分次数来控制拆分的效果
s = 'I#love#you#so#much'
words = s.split('#')
print(words)  # ['I', 'love', 'you', 'so', 'much']
words = s.split('#', 2)
print(words)  # ['I', 'love', 'you#so#much']
 #字符串字面量拼接的情况
s='See' 'you' 'tomorrow'
words = s.split()
  #Python 会自动将相邻的多个字符串字面量拼接成一个字符串。'See' 'you' 'tomorrow'会被Python解释器合并成'Seeyoutomorrow',中间没有空格
print(words)  #['Seeyoutomorrow']
print('~'.join(words))  #Seeyoutomorrow🐔"""
''' #元组没有split()方法
s='See','you','tomorrow'
words=s.split() #'tuple' object has no attribute 'split'
print(words)
print('~'.join(words))'''

 #编码和解码
"""
Python 中除了字符串str类型外，还有一种表示二进制数据的字节串类型（bytes）。所谓字节串，就是由零个或多个字节组成的有限序列。
通过字符串的encode方法，我们可以按照某种编码方式将字符串编码为字节串，我们也可以使用字节串的decode方法，将字节串解码为字符串
"""
r"""🐔a = '立源'
b = a.encode('utf-8')
c = a.encode('gbk')
print(b)                  # b'\xe7\xab\x8b\xe6\xba\x90'
print(c)                  # b'\xc1\xa2\xd4\xb4'
print(b.decode('utf-8'))  # 立源
print(c.decode('gbk'))    # 立源🐔"""

#创建集合
"""
在Python中，创建集合可以使用{}字面量语法，{}中需要至少有一个元素，因为没有元素的{}并不是空集合而是一个空字典
当然，也可以使用类构造器set来创建一个集合，可以使用set函数创建一个空集合，也可以用它将其他序列转换成集合，
例如：set('hello')会得到一个包含了4个字符的集合（重复的字符l只会在集合中出现一次）。
除了这两种方式，还可以使用生成式语法来创建集合，就像之前用生成式语法创建列表那样。
"""
"""🐔set1 = {1, 2, 3, 3, 3, 2}
print(set1)
set2 = {'banana', 'pitaya', 'apple', 'apple', 'banana', 'grape'}
print(set2)  #{'pitaya', 'grape', 'apple', 'banana'}  集合中的元素具有互异性
set3 = set('hello')
print(set3)  #{'h', 'o', 'l', 'e'}
set4 = set([1, 2, 2, 3, 3, 3, 2, 1])
print(set4)  #{1, 2, 3}
set5 = {num for num in range(1, 20) if num % 3 == 0 or num % 7 == 0}
print(set5)
set6=set(range(1, 20,3))
print(set6)🐔"""
'''
集合中的元素必须是hashable类型，所谓hashable类型指的是能够计算出哈希码的数据类型，
通常不可变类型都是hashable类型，如整数（int）、浮点小数（float）、布尔值（bool）、字符串（str）、元组（tuple）等。
可变类型都不是hashable类型，因为可变类型无法计算出确定的哈希码，所以它们不能放到集合中。
例如：我们不能将列表作为集合中的元素；同理，由于集合本身也是可变类型，所以集合也不能作为集合中的元素。
我们可以创建出嵌套列表（列表的元素也是列表），但是我们不能创建出嵌套的集合
'''

"""🐔#集合中元素的遍历 由于集合具有无序性，故不能用索引运算来实现元素的遍历，不过也可以用len()来获取集合中元素的个数
set1 = {'Python', 'C++', 'Java', 'Kotlin', 'Swift'}
for elem in set1:
    print(elem) #集合具有无序性，故每次print出的结果中元素的顺序都是不同的

#集合的运算
 #成员运算 通过in和not in判断某元素是否在集合中
set1 = {11, 12, 13, 14, 15}
print(10 in set1)  # False
print(15 in set1)  # True
set2 = {'Python', 'Java', 'C++', 'Swift'}
print('Ruby' in set2)  # False
print('Java' in set2)  # True

 #二元运算
set1 = {1, 2, 3, 4, 5, 6, 7}
set2 = {2, 4, 6, 8, 10}
  #交集
print(set1&set2)                      # {2, 4, 6}
print(set1.intersection(set2))          # {2, 4, 6}
  #并集
print(set1|set2)                      # {1, 2, 3, 4, 5, 6, 7, 8, 10}
print(set1.union(set2))                 # {1, 2, 3, 4, 5, 6, 7, 8, 10}
  #差集 两集合中相同的元素减掉，对于相异的元素，只保留减号前面的集合中的
print(set1-set2)                      # {1, 3, 5, 7}
print(set1.difference(set2))            # {1, 3, 5, 7}
  #对称差  两个集合中除开交集的部分
print(set1^set2)                      # {1, 3, 5, 7, 8, 10}
print(set1.symmetric_difference(set2))  # {1, 3, 5, 7, 8, 10}🐔"""
'''
对两个集合求交集，&运算符和intersection方法的作用是完全相同的，使用运算符的方式显然更直观且代码也更简短。
需要说明的是，集合的二元运算还可以跟赋值运算一起构成复合赋值运算，
例如：set1|=set2相当于set1=set1|set2，跟|=作用相同的方法是update；
set1&=set2相当于set1=set1&set2，跟&=作用相同的方法是intersection_update
'''

#比较运算
'''
两个集合可以用==和!=进行相等性判断，如果两个集合中的元素完全相同，那么==比较的结果就是True，否则就是False。
如果集合A的任意一个元素都是集合B的元素，那么集合A称为集合B的子集，
即对于∀𝑎∈𝐴，均有𝑎∈𝐵，则𝐴⊆𝐵，A是B的子集，反过来也可以称B是A的超集。
如果A是B的子集且A不等于B，那么A就是B的真子集。
Python为集合类型提供了判断子集和超集的运算符，其实就是我们非常熟悉的<、<=、>、>=这些运算符。
当然，我们也可以通过集合类型的方法issubset（是否子集）和issuperset（是否超集）来判断集合之间的关系
'''
"""🐔set1 = {1, 3, 5}
set2 = {1, 2, 3, 4, 5}
set3 = {5, 4, 3, 2, 1}
print(set1<set2)   #True   <子集
print(set1<=set2)  #True   <=真子集
print(set2<set3)   #False
print(set2<=set3)  #True
print(set2>set1)   #True   >超集
print(set2==set3)  #True
print(set1.issubset(set2))    #True
print(set2.issuperset(set1))  #True🐔"""

"""🐔#集合的方法 因为集合是可变类型，所以可以向集合中增删元素
set1 = {1, 10, 100}
 #添加元素
set1.add(1000)
set1.add(10000)
print(set1)  # {1, 100, 1000, 10, 10000}
 #删除元素
set1.discard(10)
if 100 in set1:
    set1.remove(100)
print(set1)  # {1, 1000, 10000}
set1.pop()  #pop方法可以从集合中随机删除一个元素，该方法在删除元素的同时会返回（获得）被删除的元素
print(set1)
 #清空元素
set1.clear()
print(set1)  # set() 前面提到过：没有元素的{}并不是空集合而是一个空字典。故此处输出的不是{}而是类构造器set()
#集合类型还有一个名为isdisjoint的方法可以判断两个集合有没有相同的元素，如果没有相同元素，该方法返回True，否则该方法返回False
set1 = {'Java', 'Python', 'C++', 'Kotlin'}
set2 = {'Kotlin', 'Swift', 'Java', 'Dart'}
set3 = {'HTML', 'CSS', 'JavaScript'}
print(set1.isdisjoint(set2))  # False
print(set1.isdisjoint(set3))  # True🐔"""

#不可变集合 frozenset
'''
可变集合set跟不可变集合frozenset的区别就如同list跟tuple的区别，
frozenset由于是不可变类型，能够计算出哈希码，因此它可以作为set中的元素。
除了不能添加和删除元素，frozenset在其他方面跟set是一样的，但在终端输出时会默认带上frozenset()的类构造器
'''
"""🐔fset1 = frozenset({1, 3, 5, 7})
fset2 = frozenset(range(1, 6))
print(fset1)          # frozenset({1, 3, 5, 7})
print(fset2)          # frozenset({1, 2, 3, 4, 5})
print(fset1&fset2)  # frozenset({1, 3, 5})
print(fset1|fset2)  # frozenset({1, 2, 3, 4, 5, 7})
print(fset1-fset2)  # frozenset({7})
print(fset1<fset2)  # False🐔"""

#创建和使用字典


























