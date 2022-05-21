"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    def string_cheker(str1, str2):

        if isinstance(str1, str) and isinstance(str2, str):
            if str1 == str2:
                return 1
            elif str1 != str2:
                if len(str1) > len(str2):
                    return 2
                elif str2 == 'learn':
                    return 3
        return 0
        
    
    a = string_cheker(123, 'asda')
    print(a)
    a = string_cheker('qwe', 'qwe')
    print(a)
    a = string_cheker('qwe', 'qw')
    print(a)
    a = string_cheker('qwe', 'learn')
    print(a)
    a = string_cheker('qweeqweqwewewqqe', 'learn123')
    print(a)
    


            
      
    
if __name__ == "__main__":
    main()
