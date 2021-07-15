import random
passord_up = input ('請輸入猜數字隨機最大值')
passord_up = int(passord_up)
passord_down = input('請輸入猜數字隨機最小值')
passord_down = int (passord_down)
password = random.randint(passord_down, passord_up)
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
		print ('您猜中密碼了')
		print ('您總計猜了', num, '次')
		break	