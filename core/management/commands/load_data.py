import locale
import datetime
import json
import requests

from django.core.management.base import BaseCommand

from core.models import Post


DATA_URL = 'https://hubofdata.ru/storage/f/2013-08-18T19%3A58%3A51.196Z/greetings-data.json'


class Command(BaseCommand):
    help = 'load data and add in database'

    def handle(self, *args, **kwargs):
        locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

        resp = requests.get(DATA_URL)
        data = json.loads(resp.text)

        Post.objects.bulk_create(
            [Post(post_id=int(item['id']),
                  category=item['category'],
                  from_whom=item['from'],
                  title=item['title'],
                  text=item['text'],
                  thedate=datetime.datetime.strptime(item['thedate'], '%d %B %Y года')) for item in data['items']],
            ignore_conflicts=True
        )

