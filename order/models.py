from django.db import models
from django.contrib.auth.models import User
from recipient.models import Recipient
from market.models import ProductSets
from enum import Enum
from django.utils import timezone
import datetime


# class OrderChoices(Enum):
#     created = 'created',
#     delivered = 'delivered',
#     processed = 'processed',
#     cancelled = 'cancelled'
#
#     @classmethod
#     def choices(cls):
#         return [(i.name, i.value) for i in cls]
#
#
# class Order(models.Model):
#     order_created_datetime = models.DateTimeField(auto_now_add=True)
#     delivery_datetime = models.DateTimeField()
#     delivery_address = models.CharField(max_length=200, verbose_name="address")
#     recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, blank=True)
#     product_set = models.ForeignKey(ProductSets, on_delete=models.CASCADE, blank=True)
#     status = models.Choices(OrderChoices, value=OrderChoices.choices())
#
#     def __str__(self):
#         return self.delivery_address
