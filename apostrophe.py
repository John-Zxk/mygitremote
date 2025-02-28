'''
first_name = "ada"
last_name = " lovelace"
full_name = first_name + last_name
print(full_name)

#字符串中添加变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
message = f"Hello, {full_name.title()}!"
print(message)

#字符串中添加制表符或换行符
print("python")
print("\tpython")

print("languages:\npython\nc\nJavaScript")
print("languages:\n\tpython\n\tc\n\tJavaScript")
print("languages:\t\npython\t\nc\t\nJavaScript")

#字符串调用方法取消右测空格rstrip
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

#字符串调用方法取消左测空格lstrip, 两侧都取消strip()

favorite_language = '  python'
favorite_language = favorite_language.lstrip()
print(favorite_language)


example：

>>> favorite_language = ' python '
>>> favorite_language.rstrip()
' python'
>>> favorite_language.lstrip()
'python '
>>> favorite_language.strip()
'python'

删除前缀， URL上使用
>>> nostarch_url = 'https://nostarch.com'
>>> nostarch_url.removeprefix('https://')
'nostarch.com'
>>> simple_url = nostarch_url.removeprefix('https://')
>>> simple_url
'nostarch.com'
>>>

'''

message = "One of Python's strengths is its diverse community."
print(message)

message = 'One of Python's strengths is its diverse community.'
print(message)


#69 Page