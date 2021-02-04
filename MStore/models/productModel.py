from django.db import models
from .categoryModel import Category


class ProductModel(models.Model):
    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, default=1)
    brand = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='', null=True, blank=True)
    image = models.ImageField(upload_to='Uploads/products/')
    rating = models.IntegerField(default=0)

    @staticmethod
    def get_all_product():
        return ProductModel.objects.all()

    @staticmethod
    def get_all_product_byCategoryId(category_id):
        if category_id:
            return ProductModel.objects.filter(category= category_id)
        else:
            return ProductModel.objects.all()

    @staticmethod
    def get_product_by_cartids(ids):
        return ProductModel.objects.filter(id__in=ids)
