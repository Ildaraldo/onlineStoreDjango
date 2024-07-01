from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        # создаём категории
        category_list = [
            {"name": "Игрушки", "description": "Игрушки для детей", "is_active": 1},
            {"name": "Товары для животных", "description": "Товары для всех животных", "is_active": 1},
            {"name": "Соки", "description": "Натуральные соки", "is_active": 1}
        ]

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        # удаляем старые записи
        Category.objects.all().delete()

        # добавляем новые записи
        Category.objects.bulk_create(category_for_create)

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

