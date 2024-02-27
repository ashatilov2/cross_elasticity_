"""

  Part of case-study #2: Task elasticity


  Задача:
  В местном супермаркете цены на мандарины выросли на 15%,
  в результате недельный обьем продаж апельсинов в этом супермаркете вырос с 2-х тонн до 2,6 тонн.
  Эластичным или неэластичным оказался спрос на апельсины по цене мандаринов?
  Какими товарами по отношению друг к другу являются эти товары?


  Developers: -----

"""

import art_local as art


def main():
    '''
    Main function.
    :return: None
    '''


print('Знаете ли вы цены на мандарины? (y - да, n - нет(цены в процентах))')
answer = input()
if answer == 'y':
    price_1 = float(input(art.count_price_1))
    price_2 = float(input(art.count_price_2))
    demand_1 = float(input(art.count_demand_1))
    demand_2 = float(input(art.count_demand_2))

    elasticity_1 = ((demand_2 - demand_1) / (demand_2 + demand_1)) * ((price_1 + price_2) / (price_2 - price_1))
    print(elasticity_1)

    if elasticity_1 > 0:
        print('товары - Субституты (взаимозаменяющие)')
    elif elasticity_1 < 0:
        print('товары -Комплименты (взаимодополняющие)')
    elif elasticity_1 == 1:
        print('товары - не зависящие друг от друга')


elif answer == 'n':
    print('увеличилась или уменьшилась цена(u - увеличилась, d - упала)')
    answer_2 = input()
    if answer_2 == 'u':
        changes_1 = float(input(art.count_changes_1))
        demand_1 = float(input(art.count_demand_1))
        demand_2 = float(input(art.count_demand_2))

        elasticity_1 = ((demand_2 - demand_1) / (demand_2 + demand_1)) * (
                (100 + (100 + changes_1)) / ((100 + changes_1) - 100))
        print(elasticity_1)

        if elasticity_1 > 0:
            print('товары - Субституты (взаимозаменяющие)')
        elif elasticity_1 < 0:
            print('товары -Комплименты (взаимодополняющие)')
        elif elasticity_1 == 1:
            print('товары - не зависящие друг от друга')

    elif answer_2 == 'd':
        changes_1 = float(input(art.count_changes_1))
        demand_1 = float(input(art.count_demand_1))
        demand_2 = float(input(art.count_demand_2))

        elasticity_1 = ((demand_2 - demand_1) / (demand_2 + demand_1)) * (
                (100 + (100 - changes_1)) / ((100 - changes_1) - 100))
        print(elasticity_1)

        if elasticity_1 > 0:
            print('товары - Субституты (взаимозаменяющие)')
        elif elasticity_1 < 0:
            print('товары -Комплименты (взаимодополняющие)')
        elif elasticity_1 == 1:
            print('товары - не зависящие друг от друга')

    else:
        print('вы ввели неверный знак')

else:
    print('вы ввели неверный знак')
