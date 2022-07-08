"""shop_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from shop_app import views


router = DefaultRouter()
router.register('Attribute', views.AttributeViewset)
router.register('AttributeName', views.AttributeNameViewset)
router.register('AttributeValue', views.AttributeValueViewset)
router.register('Catalog', views.CatalogViewset)
router.register('Image', views.ImageViewset)
router.register('Product', views.ProductViewset)
router.register('ProductAttributes', views.ProductAttributesViewset)
router.register('ProductImage', views.ProductImageViewset)


urlpatterns = [
    path('ImportAndDetail/', include(router.urls)),
]
