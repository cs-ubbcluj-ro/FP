from unittest import TestCase

from lecture.livecoding.bakery.domain.bakery_product import Product, ProductType


class TestBakeryProduct(TestCase):
    def test_bakery_product(self):
        prod = Product(100, "Bagels 500g", ProductType.BAGEL)
        self.assertEqual(100, prod.id)
        self.assertEqual(ProductType.BAGEL, prod.type)
