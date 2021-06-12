from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    query = models.CharField(max_length=500)
    date = models.DateTimeField()

    def __str__(self):
        return self.name


