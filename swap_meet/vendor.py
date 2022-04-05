from .item import Item

class Vendor():
    # create inventory parameters, where deafalt is empty list
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    
    # create instance method add which add things in inventory list
    def add(self,item):
        self.inventory.append(item)
        return item

    # create instance method remove which remove item from inventory list
    def remove(self,item):
        for items in self.inventory:
            if item == items:
                self.inventory.remove(items)
                return items
        return False

    # create instance method which return a list of Items in the inventory with that category
    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category == item.category:
                list_of_items.append(item)
        return list_of_items