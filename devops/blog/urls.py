from django.urls import path, include
from devops.blog.apis.products import ProductApi

urlpatterns = [
    path('product/', ProductApi.as_view(),name="product")
]
