salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
need_money = 0  # количество денег, чтобы прожить 10 месяцев

need_money = spend
for i in range(1, months):  # ОТСЧЕТ С НУЛЯ, ВТОРОЙ МЕСЯЦ = 1
    spend = spend + spend * increase
    need_money = need_money + spend
money = salary * months
need_money = need_money - money
print(round(need_money))
