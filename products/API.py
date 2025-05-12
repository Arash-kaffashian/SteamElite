import requests
import re


def turkey_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=TR"}"

    response = requests.get(url)
    pk = str(pk)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_1 = "Free"
        else:
            price_1 = app_data['price_overview']['final_formatted']
            price_1 = price_1.replace('$', '').replace('USD', '').strip()
            price_1 = float(price_1)

        return price_1


def brazil_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=BR"}"

    response = requests.get(url)
    pk = str(pk)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_2 = "Free"
        else:
            price_2 = app_data['price_overview']['final_formatted']
            price_2 = price_2.replace('$', '').replace('R', '').replace(',', '.').strip()
            price_2 = float(price_2)

        return price_2


def global_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=US&l=english"}"

    response = requests.get(url)
    pk = str(pk)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_3 = "Free"
        else:
            price_3 = app_data['price_overview']['final_formatted']
            price_3 = price_3.replace('$', '')
            price_3 = float(price_3)

        return price_3

