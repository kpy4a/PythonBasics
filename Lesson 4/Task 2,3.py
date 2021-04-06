"""Lesson2/3"""
from requests import get, utils
from datetime import date

response = get('http://www.cbr.ru/scripts/XML_daily.asp')


def currency_rates(currency):
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    cur_list = content.split("<Value ID=")
    rates_date = content[content.find('Date="') + 6:content.find('" name')]
    d = date(int(rates_date[6:]), int(rates_date[3:5]), int(rates_date[0:2]))
    print(d)

    for fragment in cur_list:
        if currency.upper() in fragment:
            result = fragment[fragment.find("<Value>") + 7:fragment.find("</Value>")]
            rate = float(result.replace(",", "."))
            print(rate)

            break

    if currency not in content:
        print(None)


currency_rates("USD")
currency_rates("EUR")
currency_rates("MYR")  # малайзийский ринггит
currency_rates("GHS")  # ганский седи