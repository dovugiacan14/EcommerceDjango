from django.db import models

# Create your models here.
class Categories(models.Model):
    cat_name = models.CharField(max_length= 50)
    cat_url = models.CharField(max_length= 50)

    def __str__(self):
        return self.cat_name
    
class Product(models.Model):
    pro_name = models.CharField(max_length= 100)
    original = models.CharField(max_length= 100)
    price = models.FloatField()
    pro_url = models.CharField(max_length= 10)
    id_cat = models.ForeignKey(Categories, on_delete= models.CASCADE)

    def __str__(self):
        return self.pro_name
