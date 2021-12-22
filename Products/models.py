from django.db import models
from django.shortcuts import reverse


# Модель категорий
class ProductTag(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show_necessary_tag", kwargs={"slug": self.slug})


# Модель характеристик
class Specification(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self):
        return self.title


# Модель сезонов
class Season(models.Model):
    value = models.CharField(max_length=30, unique=True)
    spec = models.ManyToManyField(Specification, blank=True, related_name="season")

    def __str__(self):
        return self.value


# Модель состава
class Composition(models.Model):
    value = models.CharField(max_length=30, unique=True)
    spec = models.ManyToManyField(Specification, blank=True, related_name="composition", )

    def __str__(self):
        return self.value


# Модель бренда
class Brand(models.Model):
    value = models.CharField(max_length=30, unique=True)
    spec = models.ManyToManyField(Specification, related_name="brand", blank=True, )

    def __str__(self):
        return self.value


# Модель размера
class Size(models.Model):
    value = models.CharField(max_length=30, unique=True)
    spec = models.ManyToManyField(Specification, blank=True, related_name="size")

    def __str__(self):
        return self.value


# Модель товара
class Product(models.Model):
    image = models.ImageField(upload_to="images/product_images/")
    title = models.CharField(max_length=30, unique=True)
    tag = models.ManyToManyField(ProductTag, related_name="products", blank=True)
    slug = models.SlugField(max_length=30, unique=True)
    price = models.PositiveSmallIntegerField()
    season = models.ForeignKey(Season, blank=True, related_name="season", on_delete=models.CASCADE)
    composition = models.ForeignKey(Composition, blank=True, related_name="composition", on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, blank=True, related_name="brand", on_delete=models.CASCADE)
    size = models.ForeignKey(Size, blank=True, related_name="size", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('show_necessary_product', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
