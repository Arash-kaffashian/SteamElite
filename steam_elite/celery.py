import os
from celery import Celery

# مسیر تنظیمات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'steam_elite.settings')

app = Celery('steam_elite')

# تنظیمات را از settings.py بخواند
app.config_from_object('django.conf:settings', namespace='CELERY')

# تسک‌ها را از اپ‌های ثبت‌شده بخواند
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')