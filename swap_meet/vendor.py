# from item import Item


class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self,item):

        self.inventory.append(item)
        return item

    def remove(self,item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            # print(item)
            if item.category == category:
                # print(item.category)
                item_list.append(item)
        return item_list



# item_a = Item(category="clothing")
# item_b = Item(category="electronics")
# item_c = Item(category="clothing")
# vendor = Vendor(
#     inventory=[item_a, item_b, item_c]
# )

# items = vendor.get_by_category("clothing")