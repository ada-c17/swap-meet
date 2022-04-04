class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        result = [item for item in self.inventory if item.category is category]
        return result

    def swap_items(self, vendor, my_item, their_item):
        if (my_item in self.inventory and
                their_item in vendor.inventory):
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            vendor.add(my_item)
        else:
            return False
        return True
