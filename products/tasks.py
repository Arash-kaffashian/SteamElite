import requests
import redis
from celery import shared_task
from django.conf import settings

cache = redis.StrictRedis(host='localhost', port=6379, db=settings.REDIS_CACHE_DB, decode_responses=True)


def update_turkey_price(pk):
    url = f"https://store.steampowered.com/api/appdetails?appids={pk}&filters=&cc=TR"
    response = requests.get(url)
    pk = str(pk)

    if response.status_code == 200:
        data = response.json()
        app_data = data[pk].get("data")

        if not app_data:
            return None

        if app_data.get("is_free"):
            price_1 = "Free"
        else:
            price_1 = app_data["price_overview"]["final_formatted"]
            price_1 = price_1.replace("$", "").replace("USD", "").strip()
            price_1 = float(price_1)

        cache_key = f"turkey_price:{pk}"
        cache.setex(cache_key, settings.CACHE_TTL, price_1)
        return price_1
    return None


@shared_task
def refresh_all_prices():
    app_ids = [730, 440, 570, 1091500]
    for pk in app_ids:
        try:
            update_turkey_price(pk)
            print(f"✅ Updated price cache for {pk}")
        except Exception as e:
            print(f"❌ Failed to update {pk}: {e}")
