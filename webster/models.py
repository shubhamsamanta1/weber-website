from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    query = models.CharField(max_length=50)
    date = models.DateTimeField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField
    Product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    auther = models.CharField(max_length=50)
    desc = models.CharField(max_length=100)
    publish_date = models.DateField()
    image = models.ImageField(upload_to='images',default="")
    file = models.FileField(upload_to="files", default="")

    def __str__(self):
        return self.Product_name


