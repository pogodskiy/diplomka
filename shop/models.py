from django.db import models
from user.models import UserModel

class Products(models.Model):
    cat = models.ForeignKey('CatProduct', on_delete=models.PROTECT)
    item_name = models.CharField(max_length=20, unique=True)
    item_detail = models.TextField(max_length=200)
    discount = models.CharField(max_length=10, choices=[('40', '40'), ('30', '30'), ('20', '20'), ('10', '10'), ('No', 'No')])
    comment = models.TextField(max_length=100)
    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, verbose_name='Поставщик', related_name='products')


class Supplier(UserModel):
    pass


class CatProduct(models.Model):
    cat_name = models.CharField(max_length=20, db_index=True)

    def __str__(self):
        return self.cat_name

