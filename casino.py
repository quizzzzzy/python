import random
user_money = 100
casino_money = 100
while user_money and casino_money:
    print("у игрока", user_money, "монет")
    print("у игрока",casino_money, "монет")
    input("нажмите enter чтобы сделать ход")
    user_turn =random.randint(1, 6)
    casino_turn =random.randint(1, 6)
    print("игрок выбросил", user_turn)
    print("казино выбросило", casino_turn)
    if casino_turn > user_turn:
        print("казино победило")
        user_money -= 1
        casino_money += 1 
    elif user_turn > casino_turn:
        print("игрок победил")
        user_money += 1 
        casino_money -= 1
    else:
        print("ничья")
        
if casino_money == 0:
    print("конец. у казино кончились деньги")
else:
    print("конец. у игрока кончились деньги")
