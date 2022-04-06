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

    def swap_items(self, another_vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in another_vendor.inventory:    
            return False
        
        another_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        another_vendor.inventory.remove(their_item)
        return True
            
    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory == []:
            return False
        self.inventory.append(friend.inventory[0])
        friend.inventory.append(self.inventory[0])
        self.inventory.remove(self.inventory[0])
        friend.inventory.remove(friend.inventory[0])
        return True

    def get_best_by_category(self, category):
        self.category = category
        highest_rank = 0.0
        for item in self.inventory:
            if self.condition == 5.0:
                if item.category == category:
                    return item
                else:
                    return None
            

    
    
            

        


        