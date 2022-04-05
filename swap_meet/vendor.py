from operator import attrgetter
from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory =None):
        if inventory is None:
            inventory =[]
        # if isinstance(inventory,list) and not inventory:
        self.inventory = inventory
        # elif all(isinstance(x, Item) for x in inventory):   
        #     self.inventory = inventory
        # else:
        #     raise ValueError ("Argument inventory should be a list of objects class Item")  
        # ! I cant add the logic above because tests in Wave1 pass the list of strings!
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            indx=self.inventory.index(item)
            item_removed=self.inventory.pop(indx)   
        else:
            return False
        return item_removed    

    def get_by_category(self, category):
        return [i for i in self.inventory if i.category ==category]  

    def swap_items(self, friend,my_item, their_item ):
        if my_item not in self.inventory or their_item not in friend.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        friend.remove(their_item)
        friend.add(my_item)
        return True

    def swap_first_item(self, friend):
        if self.inventory == [] or friend.inventory ==[]:
            return False
        my_item =self.inventory[0]    
        their_item=friend.inventory[0]
        self.swap_items(friend,my_item, their_item)
        return True

    def get_best_by_category(self, category):
        matching_category=self.get_by_category(category)
        return max(matching_category, key =attrgetter('condition'), default=None)

    def swap_best_by_category(self,other,my_priority, their_priority):
        my_best_item=self.get_best_by_category(their_priority)
        their_best_item=other.get_best_by_category(my_priority)
        if my_best_item is None or their_best_item is None:
            return False
        self.swap_items(other, my_best_item, their_best_item)
        return True

