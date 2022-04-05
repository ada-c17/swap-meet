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
        return False
    
    def get_by_category(self, category):
        output = [Item for Item in self.inventory if category == Item.category]
        return output

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.add(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            self.remove(my_item)
            return True
        return False
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            self.add(other_vendor.inventory[0]) 
            other_vendor.add(self.inventory[0])  
            self.remove(self.inventory[0]) 
            other_vendor.remove(other_vendor.inventory[0])
            return True
        return False