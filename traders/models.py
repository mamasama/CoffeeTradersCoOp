from django.db import models

class Product(models.Model):

   #CharField is fixed length text
   name = models.CharField(max_length=100)
   description = models.TextField()
   price = models.DecimalField(max_digits=10, decimal_places=2)
   image = models.ImageField(upload_to='product_images/', blank=True, null=True) 
   

   def __str__(self):
        return self.name
   
   

