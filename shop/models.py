from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class categ(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categ'

    def get_url(self):
        return reverse('prodt_cat',args=[self.slug])

class product(models.Model):
    name=models.CharField(max_length=150,unique=True)
    slug=models.SlugField(max_length=150,unique=True)
    img=models.ImageField(upload_to='photo')
    dese=models.TextField()
    stock=models.IntegerField()
    available=models.BooleanField()
    price=models.IntegerField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)

    def get_url(self):
        return reverse('detail',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.name