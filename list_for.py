# for 循环，for 变量 in 列表等支持循环的数据结构+ 冒号：代表是for 循环
# 受行必须缩进，代表是循环体， 如果在循环体内需要缩进。如果不需要循环，则不用缩进。
# 4.1 pizza
pizzas = ['chicken pizza', 'beef pizza', 'peperoni pizza', 'fruit pizza']
for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza")

# 4.2 animal
animals = ['dog', 'cat', 'tiger']
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would make a great pet!")

# 4.3 创建数值列表
for value in range(1, 5):
    print(value)

for value in range(1, 6):
    print(value)

for value in range(5):
    print(value)

for value in range(6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

# Range,step = 2，产生偶数列表
even_number = list(range(2, 11, 2))
print(even_number)

square_number = []
for value in range(1, 11):
    square = value ** 2
    square_number.append(square)
print(square_number)

square_number = []
for value in range(1, 11):
    square_number.append(value ** 2)
print(square_number)

digites = list(range(10))
print(min(digites))
print(max(digites))
print(sum(digites))

# 列表推导式 变量 = [表达式(value **2) ，for value 循环] for 循环提供值
squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 练习 4.3：数到 20
numbers = list(range(1, 21))
for number in numbers:
    print(number,end=" ")

# 练习 4.4：100 万
numbers = list(range(1, 1000001))
for number in numbers:
    print(number,end=" ")

# 练习 4.5：100 万求和
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
a = sum(numbers)
print(a)

# 练习 4.6：奇数
numbers = list(range(1,21,2))
print(numbers)

练习 4.7：3 的倍数
odd_number = []
numbers = list(range(3, 31))
for number in numbers:
    if number % 3 == 0:
        odd_number.append(number)
print(odd_number)

# 练习 4.8：立方
numbers = []
for value in range(1, 11):
    cube = value ** 3
    numbers.append(cube)
print(numbers)

# 练习 4.9：立方推导式
numbers = [value ** 3 for value in range(1, 11)]
print(numbers)

