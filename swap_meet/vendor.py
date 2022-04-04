class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)

        return category_items
    
    def swap_items(self, other_vendor, my_item, their_item):
        try:
            if my_item not in self.inventory or their_item not in other_vendor.inventory:
                raise ValueError
            self.remove(my_item)
            other_vendor.remove(their_item)

            other_vendor.add(my_item)
            self.add(their_item)
            
        except ValueError:
            return False

        return True

    def swap_first_item(self, other_vendor):
        try:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            result = self.swap_items(other_vendor, my_item, their_item)
            return result
        except IndexError:
            return False