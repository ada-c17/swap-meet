
class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        try: 
            self.inventory.remove(item)
            return item
        except ValueError as error:
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory: 
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        
        self.add(their_item)
        vendor.add(my_item)
        self.remove(my_item)
        vendor.remove(their_item)
        return True
    
    def swap_first_item(self, vendor):

        if not self.inventory or not vendor.inventory:
            return False

        self.add(vendor.inventory[0])
        vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        vendor.remove(vendor.inventory[0])
        return True


        
    