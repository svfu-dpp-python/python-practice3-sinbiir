import unittest

from product import Product


class TestProduct(unittest.TestCase):
    def test_name(self):
        name = 'Товар'
        p = Product(name, 1.0)
        self.assertEqual(p.name, name)

    def test_positive_price(self):
        new_price = 5.0
        p = Product('Товар', 1.0)
        p.set_price(new_price)
        self.assertEqual(p.get_price(), new_price)
        with self.assertRaises(TypeError):
            Product.get_price()

    def test_zero_price(self):
        old_price = 1.0
        p = Product('Товар', old_price)
        p.set_price(0.0)
        self.assertEqual(p.get_price(), old_price)

    def test_negative_price(self):
        old_price = 1.0
        p = Product('Товар', old_price)
        p.set_price(-5.0)
        self.assertEqual(p.get_price(), old_price)

    def test_positive_discount1(self):
        new_discount = 5.0
        p1 = Product('Товар1', 1.0)
        p1.set_discount(new_discount)
        p2 = Product('Товар2', 1.0)
        self.assertEqual(p1.get_discount(), new_discount)
        self.assertEqual(p2.get_discount(), new_discount)
        self.assertEqual(Product.get_discount(), new_discount)

    def test_positive_discount2(self):
        new_discount = 5.0
        p1 = Product('Товар1', 1.0)
        Product.set_discount(new_discount)
        p2 = Product('Товар2', 1.0)
        self.assertEqual(p1.get_discount(), new_discount)
        self.assertEqual(p2.get_discount(), new_discount)
        self.assertEqual(Product.get_discount(), new_discount)

    def test_negative_discount(self):
        old_discount = 0.0
        p = Product('Товар', old_discount)
        p.set_discount(-5.0)
        self.assertEqual(p.get_discount(), old_discount)
        self.assertEqual(Product.get_discount(), old_discount)
