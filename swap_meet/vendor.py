class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory
        if self.inventory == None:
            self.inventory = []
    
    def add(self, item):
        if self.inventory == None:
            self.inventory = []
            self.inventory.append(item)
        else:
            self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    
    def get_by_category(self, category):
        new_list = []
        for item in self.inventory:
            if item.category == category:
                new_list.append(item)
        return new_list

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            vendor.remove(their_item)
        else:
            return False
        vendor.add(my_item)
        self.add(their_item)
        return True



