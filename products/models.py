from django.db import models

class Product(models.Model):
    prod_created_date = models.DateTimeField(auto_now=True)
    prod_modified_date = models.DateTimeField(null=True)
    prod_is_active = models.BooleanField(default=True)
    prod_type = models.CharField(max_length=10,null=True) 
    prod_name = models.CharField(max_length=200) 
    prod_description = models.CharField(max_length=500,null=True) 
    prod_is_variation = models.BooleanField(null=True)
    prod_brand_id = models.BigIntegerField(null=True)
    prod_code = models.CharField(max_length=10,null=True) 
    prod_family = models.BigIntegerField(null=True)
    prod_is_complement = models.BooleanField(default=False)
    prod_is_delete = models.BooleanField(default=False)

    class Meta:
        managed = True
        db_table = 'product'

    def __str__(self):
        return self.prod_name

class ProductDetail(models.Model):
    detail_is_active = models.BooleanField(default=True)
    detail_is_visibility = models.BooleanField(default=True)
    detail_price = models.FloatField(null=True)
    detail_price_offer = models.FloatField(null=True) 
    detail_quantity = models.IntegerField(null=True)
    detail_sku = models.IntegerField(null=True)
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    detail_created_date = models.DateTimeField(auto_now=True)
    detail_modified_date = models.DateTimeField(null=True)
    detail_offer_day_from = models.DateTimeField(null=True)
    detail_offer_day_to = models.DateTimeField(null=True)

    class Meta:
        managed = True
        db_table = 'product_detail'

    def __str__(self):
        return self.detail_sku