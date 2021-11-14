from requests import get
import re


def currency_rates(value):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp').text
    splitted_list = (re.split("<Value>|</Value>|<CharCode>|</CharCode>|\n", response))
    value = value.upper()
    if value in splitted_list:
        value_index = int(splitted_list.index(value))
        rubles_index = value_index + 2
        result = splitted_list[rubles_index] + ' Рублей'
        print(result)
    else:
        print('None')


value = input('Введите валюту: ')

currency_rates(value)
