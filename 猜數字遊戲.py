import random
password = random.randint(1, 100)
user_password = input('請輸入一個數字')
user_password = int(user_password)
num = 1
print ('您猜了第', num, '次')
num = int(num)
while True:
	if user_password > password:
		print ('您輸入的密碼比較大')
		user_password = input('請輸入一個數字')
		user_password = int(user_password)
		num = num + 1
		print ('您猜了第', num, '次')
	elif user_password < password:
		print ('您輸入的密碼比較小')
		user_password = input('請輸入一個數字')
		user_password = int(user_password)
		num = num + 1
		print ('您猜了第', num, '次')
	else:
		num = num + 1
		print ('您猜中密碼了')
		print ('您總計猜了', num, '次')
		break