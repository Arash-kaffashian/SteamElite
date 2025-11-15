import psycopg2
import time
import os

DATABASE = {
    'NAME': os.environ.get('POSTGRES_DB', 'my_database'),
    'USER': os.environ.get('POSTGRES_USER', 'my_user'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'my_password'),
    'HOST': os.environ.get('POSTGRES_HOST', 'db'),
    'PORT': os.environ.get('POSTGRES_PORT', 5432),
}

while True:
    try:
        conn = psycopg2.connect(
            dbname=DATABASE['NAME'],
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD'],
            host=DATABASE['HOST'],
            port=DATABASE['PORT']
        )
        conn.close()
        print("Postgres is ready!")
        break
    except Exception:
        print("Waiting for Postgres...")
        time.sleep(2)
