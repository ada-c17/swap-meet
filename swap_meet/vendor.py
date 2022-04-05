from .item import Item

class Vendor:
    def __init__(self,inventory = []):
        self.inventory = inventory

    
    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
           

    def get_by_category(self,category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)
        return category_list
            

    def swap_items(self,vendor,my_item,their_item):
        if my_item in self.inventory:
            self.inventory.remove(my_item)
            vendor.inventory.append(my_item)
            return True
        else:
            return False

        if their_item in vendor.inventory:
            vendor.inventory.remove(their_item) 
            self.inventory.append(their_item)
            return True
        else:
            return False



vendor = Vendor()

        
