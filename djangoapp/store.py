from djangoapp.models import Item


class Store(object):
    items = []
    __shopping_cart = {}
    itemsLoaded = False

    def add_items(self, items):
        self.items = items

    def get_store_items(self):
        return self.items

    def __init__(self):
        if not self.itemsLoaded:
            self.items = Item.objects.all()
            self.itemsLoaded = True

    def add_to_cart(self, item, qty):
        if self.is_in_cart(item):
            self.__shopping_cart[item] += qty
        else:
            self.__shopping_cart[item] = qty

    def remove_from_cart(self, item, qty=0):
        if qty > 0:
            self.__shopping_cart[item] -= qty

        else:
            self.__shopping_cart.clear(item)

    def is_in_cart(self, item) -> bool:
        return self.__shopping_cart.__contains__(item)

    def get_cart_items(self):
        return list(self.__shopping_cart.keys())

    def get_cart_item_qty(self, item):
        if self.is_in_cart(item):
            return self.__shopping_cart[item]
        else:
            return 0

    def total_price(self, item=None) -> float:
        total_price = 0

        if item is None:
            for key in self.__shopping_cart.keys():
                total_price += key.price * self.get_cart_item_qty(key)
        else:
            total_price = item.price * self.get_cart_item_qty(item)

        return total_price

    def total_cart_info(self):
        quantities = []
        for item in self.items:
            quantities.append(self.get_cart_item_qty(item))
        return list(quantities)
