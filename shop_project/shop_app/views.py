from rest_framework import viewsets
from shop_app import models
from shop_app import serializers

from django.http import HttpResponse, JsonResponse, HttpResponseNotFound

def hello_world(request):
    return HttpResponse("Zdarec")


class AttributeViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AttributeSerializer
    queryset = models.Attribute.objects.all()


class AttributeNameViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AttributeNameSerializer
    queryset = models.AttributeName.objects.all()


class AttributeValueViewset(viewsets.ModelViewSet):
    serializer_class = serializers.AttributeValueSerializer
    queryset = models.AttributeValue.objects.all()


class CatalogViewset(viewsets.ModelViewSet):
    serializer_class = serializers.CatalogSerializer
    queryset = models.Catalog.objects.all()


class ImageViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ImageSerializer
    queryset = models.Image.objects.all()


class ProductViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ProductAttributesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductAttributesSerializer
    queryset = models.ProductAttributes.objects.all()


class ProductImageViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ProductImageSerializer
    queryset = models.ProductImage.objects.all()

