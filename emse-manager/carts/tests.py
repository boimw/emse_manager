from django.test import TestCase
import unittest
from carts.cart import Cart

# Create your tests here.


class testCart(TestCase):

    def test_count(self):
        cart.self = cart
        self.assertEqual(Cart.count(self),1)

    def test_add(self):
        cart.self = cart
        assert Cart.add(self,product,quantity,unit_price) == True

    def test_remove(self):
        cart.self = cart
        assert Cart.remove(self,product) == True

    def test_add(self):
        cart.self = cart
        assert Cart.add(self,product,quantity,unit_price) == False

    def test_remove(self):
        cart.self = cart
        assert Cart.remove(self,product) == False

    def test_update(self):
        cart.self = cart
        assert Cart.update(self,product,quantity,unit_price) == True

    def test_summary(self):
        cart.self = cart
        self.assertEqual(Cart.summary(self),1)

    def test_remove(self):
        cart.self = cart
        assert Cart.clear(self) == True

if __name__ == '__main__':    unittest.main()