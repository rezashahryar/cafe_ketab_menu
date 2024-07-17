from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    logo = models.ImageField(upload_to='category_img/')

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products-image/', null=True)
    slug = models.SlugField()
    price = models.PositiveIntegerField()

    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
