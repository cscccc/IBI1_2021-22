def calculator(money, price):
    num = int(money) // int(price)
    money_left = int(money) % int(price)
    print(f'can buy {num} bars, and left {money_left}')
money = input('how much money you have:')
price = input("how much a bar is:")
calculator(money,price)
