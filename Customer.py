from User import User
from Cart import Cart
class Customer(User):
    def __init__(self, name, pw, em, phone, q, a):
        User.__init__(self, name, pw, em, phone, q, a)
        self.cart = Cart(name)

    def getCart(self):
        return self.cart

    def regetCart(self):
        self.cart = Cart(self.getName())