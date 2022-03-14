from django.db import models

# Create your models here.
class Product(models.Model):
    title =models.TextField()
    description =models.TextField()
    price =models.TextField()
    summary =models.TextField(default="All right!")
    def __str__(self):
        return self.title
    timestamp=models.DateTimeField(auto_now=False,auto_now_add=True)
    updated=models.DateTimeField(auto_now=True,auto_now_add=False)

