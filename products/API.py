import requests
import re
import redis
from steam_elite import settings
from .tasks import update_turkey_price


# اتصال به Redis برای کش
cache = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB_CACHE,
    decode_responses=True
)


def turkey_price(pk):
    """تابع معمولی برای گرفتن قیمت از کش"""
    cache_key = f"turkey_price:{pk}"
    cached_value = cache.get(cache_key)

    if cached_value:
        return float(cached_value) if cached_value != "Free" else "Free"
    else:
        # اگر کش خالی بود (مثلاً بار اول)
        return update_turkey_price(pk)


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

