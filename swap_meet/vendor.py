from operator import invert

from swap_meet.item import Item

class Vendor:    
    def __init__(self,inventory=None):
        #super(). __init__ (category)
        if not inventory:
            inventory=[]
        self.inventory=inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            #raise ValueError
            return False  

    def get_by_category(self, category):
        
        items = []
        for i in self.inventory:
            if category==i.category:
                items.append(i)
        return items
       
        # if not category in self.inventory:
        #     self.inventory
        #     return category
        #     #self.inventory.append(category)
        # #return self.inventory         

        