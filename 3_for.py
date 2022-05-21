"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sell_phones = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    
    all_sales_count = 0
    all_sales_sum = 0
    for phone in sell_phones:

        sales_sum = 0
        sales_counter = 0

        for sales in phone['items_sold']:
            sales_counter += 1
            sales_sum += int(sales)

        all_sales_count += sales_counter
        all_sales_sum += sales_sum
        avg_sales = sales_sum / sales_counter
        phone_name = phone['product']
        print(f'Продано телефонов {phone_name}:  {sales_sum} штук')
        print(f'Среднее количество продаж для {phone_name}: {round(avg_sales, 0)} штук')

    avg_sales_all = all_sales_sum / all_sales_count
    print(f'Суммарное количество продаж: {all_sales_sum} штук')
    print(f'Среднее количество продаж всех товаров: {avg_sales_all} штук')






    
    
    


    
if __name__ == "__main__":
    main()
