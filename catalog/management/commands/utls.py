from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_for_create = []
        product_for_create = []
        with open("dump_catalog.json", 'r', encoding='utf-16') as rfile:
            json_data = json.load(rfile)
            for data in json_data:
                if data['model'] == 'catalog.category':
                    category_for_create.append(Category(**data))
                elif data['model'] == 'catalog.product':
                    product_for_create.append(Product(**data))
        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)
