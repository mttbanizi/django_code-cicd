from django.db.models import QuerySet
from devops.blog.models import Product

def get_product() ->QuerySet(Product):
    return Product.objects.all()