country = input('請輸入你的國家:')
age = input('請輸入你的年齡:')
age = int(age)
if country =='台灣':
	if age >= 18:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
elif country =='美國':
	if age >= 16:
		print('你可以考駕照')
	else:
		print('你還不能考駕照')
else:
	print('你只能輸入台灣或美國')
	