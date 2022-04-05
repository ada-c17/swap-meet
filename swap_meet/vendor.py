class Vendor:
    def __init__(self, inventory=None):  # mutable type can't be used as default value
        if inventory is None:
            inventory = []
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

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None

        condition, output = -1, None
        for item in items:
            if item.condition > condition:
                condition = item.condition
                output = item
        return output

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        if my_item is None or their_item is None:
            return False
        
        return self.swap_items(other, my_item, their_item)
