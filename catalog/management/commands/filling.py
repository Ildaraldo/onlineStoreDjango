from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # загружаем все категории
        categories = Category.objects.all()

        product_list = [
            {"name": "Плю44шевая мишка", "description": "Плюшевая мишка для детей", "category": categories[0], "price": 100},
            {"name": "Косточка", "description": "Косточка для собаки", "category": categories[1], "price": 12},
            {"name": "Сок натуральный", "description": "0.5 л", "category": categories[2], "price": 22}
        ]

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(Product(**product_item))

        # удаляем старые записи
        Product.objects.all().delete()

        # добавляем новые записи
        Product.objects.bulk_create(product_for_create)

