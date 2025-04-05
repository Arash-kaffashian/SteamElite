import requests


def turkey_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=TR"}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_1 = "Free"
        else:
            price_1 = app_data['price_overview']['final_formatted']
        return price_1


def brazil_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=BR"}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_2 = "Free"
        else:
            price_2 = app_data['price_overview']['final_formatted']

        return price_2


def global_price(pk):
    url = f"{"https://store.steampowered.com/api/appdetails?appids="}{pk}{"&filters=&cc=US&l=english"}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk]['data']

        if app_data['is_free']:
            price_3 = "Free"
        else:
            price_3 = app_data['price_overview']['final_formatted']

        return price_3
