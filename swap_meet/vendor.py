from re import A
from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory = None):
        if inventory == None:
            self.inventory =[]
        else:
            self.inventory = inventory
        
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        items=[]
        for item in self.inventory:
            if str(item.category) == category:
                items.append(item)
        return items

    def swap_items(self, other_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in other_vendor.inventory:    
            return False
        
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.remove(their_item)
        return True
            
    
            

        


        