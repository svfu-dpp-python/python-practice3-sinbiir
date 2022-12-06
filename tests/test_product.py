import unittest

from product import Product


class TestProduct(unittest.TestCase):

    def test_name(self):
        name = 'Товар'
        p = Product(name, 1.0)
        self.assertEqual(p.name, name)

    def test_price(self):
        price = 1.0
        p = Product('Товар', price)
        self.assertEqual(p.get_price(), price)

    def test_positive_price(self):
        new_price = 5.0
        p = Product('Товар', 1.0)
        p.set_price(new_price)
        self.assertEqual(p.get_price(), new_price)

    def test_price_not_readable_with_class(self):
        with self.assertRaises(TypeError):
            Product.get_price()

    def test_price_not_writable_with_class(self):
        with self.assertRaises(TypeError):
            Product.set_price(1.0)

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
        p = Product('Товар', 1.0)
        old_discount = p.get_discount()
        p.set_discount(-5.0)
        self.assertEqual(p.get_discount(), old_discount)
        self.assertEqual(Product.get_discount(), old_discount)

    def test_property(self):
        p = Product('Товар', 100.0)
        p.set_discount(10.0)
        self.assertAlmostEqual(p.current_price, 90.0)
