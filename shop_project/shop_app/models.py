from django.db import models
from django.contrib.postgres.fields import ArrayField


class Attribute(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev_atributu_id = models.IntegerField(null=True, blank=True)
    hodnota_atributu_id = models.IntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.id} {self.nazev_atributu_id} {self.hodnota_atributu_id}"


class AttributeName(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=256, blank=True)
    kod = models.CharField(max_length=256, blank=True)
    zobrazit = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.id} {self.nazev} {self.kod} {self.zobrazit}"


class AttributeValue(models.Model):
    id = models.IntegerField(primary_key=True)
    hodnota = models.CharField(max_length=256, blank=True)


    def __str__(self):
        return f"{self.id} {self.hodnota}"


class Catalog(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=256, blank=True)
    obrazek_id = models.IntegerField(null=True, blank=True)
    products_ids = models.CharField(max_length=256, blank=True)
    attributes_ids = models.CharField(max_length=256, blank=True)
    #sqlite3 nepodporuje datový typ list - proto ručně změněno na str
    # products_ids = ArrayField(models.IntegerField(null=True), default=list, blank=True)
    # attributes_ids = ArrayField(models.IntegerField(null=True), default=list, blank=True)


    def __str__(self):
        return f"{self.id} {self.nazev} {self.obrazek_id} {self.products_ids}{self.attributes_ids}"


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    obrazek = models.CharField(max_length=256, blank=True)
    nazev = models.CharField(max_length=256, blank=True)


    def __str__(self):
        return f"{self.id} {self.obrazek} {self.nazev}"


class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    nazev = models.CharField(max_length=512, blank=True)
    cena = models.CharField(max_length=32, blank=True)
    mena = models.CharField(max_length=8, blank=True)
    published_on = models.DateTimeField(null=True, blank=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.nazev} {self.cena} {self.mena} {self.published_on} {self.is_published}"


class ProductAttributes(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.IntegerField()
    product = models.IntegerField()


    def __str__(self):
        return f"{self.id} {self.attribute} {self.product}"


class ProductImage(models.Model):
    id = models.IntegerField(primary_key=True)
    product = models.IntegerField()
    obrazek_id = models.IntegerField()
    nazev = models.CharField(max_length=64, blank=True)


    def __str__(self):
        return f"{self.id} {self.product} {self.obrazek_id} {self.product}"
