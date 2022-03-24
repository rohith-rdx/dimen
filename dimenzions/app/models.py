from django.db import models

# Create your models here.

class categories(models.Model):
    cat_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=255)
    category_logo = models.ImageField(default = "default.png", upload_to="images")
    sub_category1 = models.CharField(max_length=255)
    sub_category2 =  models.CharField(max_length=255)
    sub_category3 = models.EmailField(max_length=255)
    sub_category4 = models.CharField(max_length=255)
    sub_category5 = models.CharField(max_length=255)
    