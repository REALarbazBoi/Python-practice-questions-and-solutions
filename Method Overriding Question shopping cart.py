class Orders:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)

    def remove(self, item):
        self.cart.remove(item)

    def __len__(self):
        return len(self.cart)

    def __str__(self):
        items = "Cart contents: "
        for i in self.cart:
            items += i + ", "
        return items

o = Orders()
o.add_to_cart("soap")
o.add_to_cart("deo")
o.add_to_cart("brush")
print(o)
print(len(o))
o.remove("deo")
print(o)