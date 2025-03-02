# 按首字母排序，永久的改变元素的排列顺序。reverse 是按字母顺序相反排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# 按首字母反向排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# 使用sorted函数临时改变列表顺序，reverse 是按字母顺序相反排列
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))

print("\nHere is the original list again:")
print(cars)

# 反向打印列表,翻转列表,永久改变
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# 确定列表的长度
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))


# 3.8 放眼世界
citys =['dubai', 'thailand', 'canada', 'beijing', 'hangzhou']
print(citys)
print(sorted(citys))
print(citys)
print(sorted(citys,reverse=True))
print(citys)
citys.reverse()
print(citys)
citys.reverse()
print(citys)
citys.sort()
print(citys)
citys.sort(reverse=True)
print(citys)

3.9 晚餐嘉宾
guets = ['john', 'peter','kevin','judi']
print(f"Welcome {guets[0].title()} to join the dinner ")
print(f"Welcome {guets[1].title()} to join the dinner ")
print(f"Welcome {guets[2].title()} to join the dinner ")
print(f"Welcome {guets[3].title()} to join the dinner ")
print(len(guets))

# 3.10 尝试使用各个函数

tests = ['chinese', 'english','mon', 'sanxia','xihu', 'haerbin']
print(tests)
# append and insert 添加元素
tests.append('byd')
tests.insert(1,'xiaomi')
print(tests)
print(len(tests))
# del 删除元素，pop 弹出最后的元素
del tests[1]
print(tests)
print(len(tests))
tests.pop()
print(tests)
tests.append('byd')
print(tests)
# remove 按元素的值删除元素
tests.remove('byd')
print(tests)
# sort 按字母顺序排序
tests.sort()
print(tests)
# 按字母反向排序
tests.sort(reverse=True)
print(tests)

# sorted 按字母排序，临时
print(sorted(tests))
print(tests)
tests.reverse()
print(tests)

# 列表长度函数
print(len(tests))


