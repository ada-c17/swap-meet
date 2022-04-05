class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.remove(my_item)
            vendor.add(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            return True

    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]
