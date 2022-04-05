from .item import Item

class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory


    def add(self, item):
        self.inventory.append(item)
        return item
        

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False 

        # if item not in self.inventory:
        #     return False
        # self.inventory.remove(item)
        # return item


    def get_by_category(self, category):
        inventory_by_category = [] 
        for item in self.inventory:
            if item.category == category:
                inventory_by_category.append(item)
        # if item.category != category:
        #     return False 
        #return inventory_by_category
        
        if len(inventory_by_category) > 0:
            return inventory_by_category
        else:
            return False 
                
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            return True 
        return False 
    # def swap_items(self, friend, my_item, their_item):
    #     for item in self.inventory:
    #         if item == my_item:
    #             friend.inventory.append(item)
    #             self.inventory.remove(item)
    #     for item in friend.inventory:
    #         if item == their_item:
    #             self.inventory.append(item)
    #             friend.inventory.remove(item)
    #     return True 

