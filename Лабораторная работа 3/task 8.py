money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

money = money_capital + salary
while money > 0:  # ПОКА ЕСТЬ ДЕНЬГИ, БУДЕТ РАБОТАТЬ ЦИКЛ И УБАВЛЯТЬ ОБЩЕЕ КОЛ-ВО MONEY
    money = money - spend
    spend = spend + spend * increase
    month = month + 1

print(month)
