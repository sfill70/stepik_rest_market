from recipient.models import Recipient
from recipient.util_recipient import recipients_url
from market.models import ProductSets
from market.util_market import beauty_url, food_url, presents_url
from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import requests

"""ProductSets (набор продуктов):
title (заголовок или наименование) — CharField;
description (описание) — TextField;
"""

"""Recipient (получатель):
surname (фамилия) — CharField;
name (имя) — CharField;
patronymic (отчество) — CharField;
phone_number (телефон) — CharField."""

url_product_list = [beauty_url, food_url, presents_url]
json_product = []
for url in url_product_list:
    tmp_json = requests.get(url, timeout=10).json()
    for product in tmp_json:
        json_product.append(product)

json_recipient = [recipient for recipient in requests.get(recipients_url, timeout=10).json()]

class Command(BaseCommand):
    help = 'Load data from JSON to DB'

    def handle(self, *args, **options):

        try:
            for recipient in json_recipient:
                Recipient.objects.create(surname=recipient['info']['surname'],
                                         name=recipient['info']['name'],
                                         patronymic=recipient['info']['patronymic'],
                                         phone_number=recipient['contacts']['phoneNumber']
                                         )
        except Exception as e:
            print(e)

        try:
            for product in json_product:
                ProductSets.objects.create(title=product['name'],
                                          description=product['about']
                                           )
        except Exception as e:
            print(e)

        self.stdout.write(self.style.SUCCESS('Ok'))

# class Command(BaseCommand):
#     help = 'Load data from data.py file to DB'
#
#     def handle(self, *args, **options):
#
#         for company in data.companies:
#             Company.objects.create(name=company['title'])
#
#         for specialty in data.specialties:
#             Speciality.objects.create(code=specialty['code'],
#                                       title=specialty['title'],
#                                       picture='https://place-hold.it/100x60')
#
#         for job in data.jobs:
#             company = Company.objects.get(name=job['company'])
#             speciality = Speciality.objects.get(code=job['cat'])
#             Vacancy.objects.create(
#                 title=job['title'],
#                 speciality=speciality,
#                 company=company,
#                 description=job['desc'],
#                 salary_min=int(job['salary_from']),
#                 salary_max=int(job['salary_to']),
#                 published_at=datetime.strptime(job['posted'], '%Y-%m-%d'))
#
#         self.stdout.write(self.style.SUCCESS('Ok'))
