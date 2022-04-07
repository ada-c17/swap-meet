from curses import wrapper
from re import T
from signal import set_wakeup_fd
from pytest import Item
from swap_meet.item import Item 



class Vendor:
    def __init__(self, inventory =  None):
        if inventory == None:
            inventory = list(())
        self.item = Item()
        self.inventory = inventory

            
    def add(self, item):
        self.item = item 
        self.inventory.append(item)
        return item 

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        else:
            return False

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)
        return category_list
    
    def swapping (self, vendor, my_item, their_item):
        vendor.inventory.append(my_item)
        vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
   
    
    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.swapping(vendor, my_item, their_item)
            return True
        else:
            return False


    def swap_first_item(self, vendor):
        if self.inventory and vendor.inventory:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swapping(vendor, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if bool(category_items) == False:
            return None
        catergory_best = category_items[0]

        for index, item in enumerate(category_items):
            if item.condition > catergory_best.condition:
                catergory_best = item
        return catergory_best

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_catergory_best = other.get_best_by_category(my_priority)
        my_catergory_best = self.get_best_by_category(their_priority)
        
        if bool(my_catergory_best) == False or bool(their_catergory_best) == False :
            return False
        else:
            self.swap_items(other, my_catergory_best, their_catergory_best)
            return True

