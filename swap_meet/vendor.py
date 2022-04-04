class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item) 
        except ValueError:
            return False
        return item

    def get_by_category(self, category_name):
        return [item for item in self.inventory if item.category == category_name]

    def swap_items(self, vendor, my_item, their_item):     
        if not (my_item in self.inventory and their_item in vendor.inventory):
            return False
        self.inventory.append(vendor.remove(their_item))
        vendor.inventory.append(self.remove(my_item))
        return True

    def swap_first_item(self, vendor):
        if self.inventory == [] or vendor.inventory == []:
            return False
        return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])