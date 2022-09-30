import random
import os
name = input("введите имя героя")
way_1 =  True
way_2 = True
way_3 = True
game = True
key = ""
while game:

    if (way_1 or way_2 or way_3) and key == "":
        print("текст у камня")
        if way_1:
            print("1 - первый выбор")
        if way_2:
            print("2 - второй выбор")
        if way_3:
            print("3 - третий выбор")
        user_choice = input("введите номер ответа и нажмите клавишу Enter")
        key += user_choice  # ключ добвляется, если выбор известен

    if way_1 and key == "1":
        os.system("cls")
        print("текст дороги 1")
        print("1 - первый выбор")
        print("2 - второй выбор")
        user_choice = input("введите номер ответа и нажмите клавишу Enter")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_1 and key == "11":
        os.system("cls")
        print(" текст дороги 1 - хороший выбор")
        key = ""
        way_1 = False
        input("ENTER - дальше")

    if way_1 and key == "12":
        os.system("cls")
        print("текст дороги 1 - плохой выбор")
        game = False
        input("pause")


    if way_2 and key == "2":
        os.system("cls")
        print("текст дороги 2")
        print("1 - первый выбор")
        print("2 - второй выбор")
        user_choice = input("введите номер ответа и нажмите клавишу Enter")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_2 and key == "21":
        os.system("cls")
        print(" текст дороги 2 - хороший выбор")
        key = ""
        way_2 = False
        input("ENTER - дальше")
        
    
    if way_2 and key == "22":
        os.system("cls")
        print("текст дороги 2 - плохой выбор")
        game = False
        input("pause") 

    if way_3 and key == "3":
        os.system("cls")
        print("текст дороги 3")
        print("1 - первый выбор")
        print("2 - второй выбор")
        user_choice = input("введите номер ответа и нажмите клавишу Enter")
        if user_choice == "1" or user_choice == "2":
            key += user_choice

    if way_3 and key == "31":
        os.system("cls")
        print(" текст дороги 3 - хороший выбор")
        key = ""
        way_3 = False
        input("ENTER - дальше")
        
    
    if way_3 and key == "32":
        os.system("cls")
        print("текст дороги 3 - плохой выбор")
        game = False
        input("pause")

    if way_1 = False
       way_2 = False
       way_3 = False

