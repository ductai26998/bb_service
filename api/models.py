import uuid

from base.models import TimeStampedModel
from django.db import models
from base.models import MoneyField
from django.conf import settings


class Service(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)


class ServiceSalon(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    salon = models.Field(default=None)
    service = models.Field(default=None)
    price_amount = models.DecimalField(
        max_digits=settings.DEFAULT_MAX_DIGITS,
        decimal_places=settings.DEFAULT_DECIMAL_PLACES,
        default=0,
    )
    currency = models.CharField(
        max_length=settings.DEFAULT_CURRENCY_CODE_LENGTH,
        default=settings.DEFAULT_CURRENCY,
    )
    price = MoneyField(amount_field="price_amount", currency_field="currency")
