#3.4 嘉宾名单
guets = ['john', 'peter','kevin','judi']
print(f"Welcome {guets[0].title()} to join the dinner ")
print(f"Welcome {guets[1].title()} to join the dinner ")
print(f"Welcome {guets[2].title()} to join the dinner ")
print(f"Welcome {guets[3].title()} to join the dinner ")

#3.5 修改嘉宾名单
guets = ['john', 'peter','kevin','judi']
print(f"Welcome {guets[0].title()} to join the dinner ")
print(f"Welcome {guets[1].title()} to join the dinner ")
print(f"Welcome {guets[2].title()} to join the dinner ")
print(f"Welcome {guets[3].title()} to join the dinner ")
print(f"{guets[1].title()} can't join the dinner ")
guets[1] = "Vivan"
print(f"Welcome {guets[1].title()} to join the dinner ")

#3.6 添加嘉宾 & 3.7 缩短名单
guets = ['john', 'peter','kevin','judi']
print('find a big tables')
guets.insert(0,'Tom')
guets.insert(2, 'Huang')
guets.append('Zhao')
print(f"Welcome {guets[0].title()} to join the dinner ")
print(f"Welcome {guets[1].title()} to join the dinner ")
print(f"Welcome {guets[2].title()} to join the dinner ")
print(f"Welcome {guets[3].title()} to join the dinner ")
print(f"Welcome {guets[4].title()} to join the dinner ")
print(f"Welcome {guets[5].title()} to join the dinner ")
print(f"Welcome {guets[6].title()} to join the dinner ")
print('-------------------------------------------------')
print('The table can not deliver')
uninvited1 = guets.pop()
print(f"{uninvited1} can't come to diner")
uninvited2 = guets.pop()
print(f"{uninvited2} can't come to diner")
uninvited3 = guets.pop()
print(f"{uninvited3} can't come to diner")
uninvited4 = guets.pop()
print(f"{uninvited4} can't come to diner")
uninvited5 = guets.pop()
print(f"{uninvited5} can't come to diner")
print(f"Welcome {guets[0].title()} to join the dinner ")
print(f"Welcome {guets[1].title()} to join the dinner ")
del guets[-1]
del guets[-1]
print(guets)