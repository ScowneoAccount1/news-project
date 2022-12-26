from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:10]}'

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()



class News(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=100, null=True)
    text = models.TextField(null=True)
    rating = models.IntegerField()
    author_name = models.TextField(null=True)
    # в прошлом задании насколько я помню ничего не говорилось про авторов, поэтому я сделал такое быстрое/временное решение