from django.db import models


class Product(models.Model):
    class Meta:
        db_table = 'product'

    title = models.CharField(verbose_name='Наименование', max_length=120, null=False, blank=False)
    amount = models.IntegerField(verbose_name='Количество', null=False, blank=False, default=1)
    is_bought = models.BooleanField(verbose_name='Куплен', null=False, default=False)
