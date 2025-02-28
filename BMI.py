height = float(input("请输入身高（M):"))
weight = float(input("请输入体重（KG):"))
BMI = weight / height**2
print(BMI)
if BMI <= 18.4:
    print("偏瘦")
elif 23.9 >= BMI >= 18.5:
    print("正常")
elif 27.9 >= BMI >= 24:
    print("过重")
else:
    print("肥胖")


