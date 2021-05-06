from typing import Any


# Задача 1. Найти количество различных элементов массива. Пример: для [1 4 5 1 1 3] ответ 4.
def count_unique_elems(arr) -> int:
    pass


# Задача 2. Дан файл с логинами и паролями. Найдите топ10 самых популярных паролей.
# Ссылка на файл: https://yadi.sk/i/6ywJqzm93HGmy9
def get_10_popular_password(file: str) -> Any:
    pass


# Задача 3. Дана строка с ссылками. Заменить все ссылки на ***** (5 звёздочек).
# Примеры ссылок:
# www.site.com заменится на *****
# http://example.su заменится на *****
# vk.ru заменится на *****
# https://example.com/smth/else заменится на *****
# и т.д.
# Чем больше разных вариантов будет придумано, тем лучше, но без фанатизма.
# Для простоты, ограничьте набор доменов верхнего уровня (штуки 4-7 достаточно).
def censor_link(string: str) -> None:
    lst_str = string.split()
    print(lst_str)
    with open('domains.txt', 'r', encoding='utf-8') as file:
        domains = file.read().split()
        for word in lst_str:
            for domain in domains:
                if domain in word:
                    word_index = lst_str.index(word)
                    lst_str.pop(word_index)
                    if word[-1] != domain[-1] and word[-1] != '/':
                        punctuation = word[-1]
                        lst_str.insert(word_index, ' ***** ' + punctuation)
                    else:
                        lst_str.insert(word_index, ' ***** ')
        result = ''.join(lst_str)
        print(f'Checked str: {result}')



# Здесь писать тесты для функций с решениями
def main():
    print('What do you want me to do? (1 - "get_fib", 2 - "get_index", 3 - "get_skipped_num"')
    number = int(input('Enter the number please: '))
    if number == 1:
        pass
    elif number == 2:
        pass
    elif number == 3:
        urls = 'Adahf https://yandex.ru/ mahgdjh gajh dgajhd  aj.a d gjya djahd ajkdg https://yandex.ru/. ' \
               'https://www.kommersant.ru/doc/4801547?utm_source=yxnews&utm_medium=desktop'
        print(urls)
        censor_link(urls)
    else:
        print(f"I don't understand what kind of def you want me to do...")


if __name__ == '__main__':
    main()
