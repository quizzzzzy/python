import random
import os
name = input("введите имя героя")
way_1 =  True
way_2 = True
way_3 = True
game = True
key = ""
while game:
    if way_1 or way_2 or way_3:
     print("текст у камня")
    if way_1:
     print("1 - первый выбор")
    if way_2:
     print("2 - второй выбор")
    if way_3:
     print("3 - третий выбор")
    user_choice = input("введите номер ответа и нажмите клавишу Enter")
    key += user_choice
    print(key)
    input("pause")
    
    if way_1 and key == "1":
        os.sistem("cls")
        print("текст дороги один")
        print("1 - первый выбор")
        print("2 - второй выбор")
user_choice = input("введите номер ответа и нажмите клавишу Enter")
key += user_choice

if way_1 and key == "11":
    os.sistem("cls")

    
        
        
    
        
        
        
            
    
    
        
    
    
