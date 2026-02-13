# for x in range(1, 10):
# 		print(x)


# for x in range(1, 21):
# 	print("x =", x, "x² =", x*x)


# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for n in nums:
# 	if (n % 2 == 1):
# 		print(n)


# user_login = "adam"
# user_password = "Qwerty123456"

# login = input("Login: ")
# password = input("Password: ")

# if (login == user_login) and (password == user_password):
#     print("Добро пожаловать")
# else:
#     print("Неверный логин или пароль")

# employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]

# print(employee_list[1] + ', ' + employee_list[-2])

# dev_by_three = input('Введите число')
# num = int(dev_by_three)

# if (num % 3 == 0):
# 	print('Да')
# else:
# 	print('Нет')



def dev_by_three(number):
    return "Да" if number % 3 == 0 else "Нет"

num = int(input("Введите число: "))
result = dev_by_three(num)
print(f"Делится ли на три {num}? - {result}")