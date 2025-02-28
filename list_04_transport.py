# first list 第一个列表,使用方括号，元素之间用逗号分割。是有序的集合。列表（list）由一系列按特定顺序排列的元素组成。
motocycles = ['honda', 'yamaha','suzuki']
print(motocycles)
motocycles[0] = 'ducti'
print(motocycles)

# 定义空列表，在列表末尾添加新元素
motocycles = ['honda', 'yamaha','suzuki']
print(motocycles)
motocycles.append('ducti')
print(motocycles)

# 定义空列表，在列表末尾添加新元素
motocycles = []
motocycles.append('honda')
motocycles.append('yamaha')
motocycles.append('suzuki')
print(motocycles)

# 使用insert(index, object) 在任意位置添加元素
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
motocycles.insert(1, 'ducati')
print(motocycles)


# 删除元素 del函数
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
del motocycles[0]
print(motocycles)

# 删除元素，POP弹出末尾的元素
motocycles = ['honda', 'yamaha', 'suzuki']
print(motocycles)
popped_motocycle = motocycles.pop()
print(motocycles)
print(popped_motocycle)

# 可以弹出元素赋值，表示弹出的元素 POP
motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}")

# 弹出的元素可以指定元素位置POP
motocycles = ['honda', 'yamaha', 'suzuki']
last_owned = motocycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}")

#不知道删除元素的位置，根据值删除remove 
motocycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles)
motocycles.remove('ducati')
print(motocycles)

motocycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motocycles)
too_expensive = 'ducati'
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
