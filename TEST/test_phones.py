import pytest
import allure
import re
import time


def test_phones(app):

    lst =  app.contact.get_contact_list_AB() # Получаем список контактов с основной страницы:

    # Проходим по списку и печатаем все элементы:
    # lst_len = app.contact.count()            # Получаем длину списка
    # i = lst_len
    # print("\n")
    # for element in lst:
    #     if element is None:
    #         print("!!! lst[%s] = None !!!\n" % i)
    #     else:
    #         print("lst[%s] == " % i)
    #         print(element)
    #     i = i - 1
    # # End for
    # print("\n")

    #print("ПРОВЕРКА...\n")
    contact_from_home_page = lst[0]  # Берем первый элемент списка контактов
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)  # Берем первый элемент со страницы Edit контакта

    # if contact_from_edit_page is None:
    #     print("!!! edit[0] = None !!!\n")
    # else:
    #     print("edit[0] == ")
    #     print(contact_from_edit_page)
    #
    # if contact_from_home_page is None:
    #     print("!!! lst[0] = None !!!\n")
    # else:
    #     print("lst[0] == ")
    #     print(contact_from_home_page)

    tmpA = clear(contact_from_edit_page.home_phone)
    tmpB = clear(contact_from_home_page.home_phone)

    with allure.step(f'Comparing 1 assert tmpA{tmpA} & tmpB{tmpB}'):
        Flag1 = ( tmpA == tmpB )
        if Flag1 is False:
            print("Flag1: False\n")
            print(contact_from_home_page)
            print(contact_from_edit_page)
        assert Flag1

    tmpA = clear(contact_from_edit_page.work_phone)
    tmpB = clear(contact_from_home_page.work_phone)

    with allure.step(f'Comparing 2 assert tmpA={tmpA} & tmpB{tmpB}'):
        Flag2 = (tmpA == tmpB )
        if Flag2 is False:
            print("Flag2: False\n")
            print(contact_from_home_page)
            print(contact_from_edit_page)
        assert Flag2

    tmpA = clear(contact_from_edit_page.mobile_phone)
    tmpB = clear(contact_from_home_page.mobile_phone)

    with allure.step(f'Comparing 3 assert tmpA={tmpA} & tmpB={tmpB}'):
        Flag3 = ( tmpA ==  tmpB )
        if Flag3 is False:
            print("Flag3: False\n")
            print(contact_from_home_page)
            print(contact_from_edit_page)
        assert Flag3

    tmpA =  clear(contact_from_edit_page.second_home)
    tmpB = contact_from_home_page.second_home

    with allure.step(f'Comparing 4 assert tmpA{tmpA} & tmpB{tmpB}'):
        Flag4 = ( tmpA == tmpB )
        if Flag4 is False:
            print("Flag4: False\n")
            print(contact_from_home_page)
            print(contact_from_edit_page)
        assert Flag4


def clear(stroka): # Удаляем символы ( ) - из строк s используя модуль регулярных выражений re

    if stroka is None:
        print("ERROR: string is empty!\n")
        return None
    else:
        return re.sub("[+() -.]", "", stroka)



