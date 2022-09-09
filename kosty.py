import random

user = random.randint(1, 6)  # пользователь: выкинуть от 1 до 6 включительно
cpu = random.randint(1, 6) # комп: выкинуть от 1 до 6 включительно
 
print("Пользователь выбросил", user)
print("Компьютер выбросил", cpu)

if cpu > user: #  у компа больше
	print("Компьютер победил!")
elif user > cpu: # у пользователя больше
	print("Пользователь победил!")
else: #  ничья
	print("Ничья!")	
    
    	

