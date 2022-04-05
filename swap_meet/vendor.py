from operator import invert
from tokenize import maybe

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
       
    def swap_items(self,friend,my_item,their_item):
        my_inventory=self.inventory
        friends_inventory=friend.inventory

        if my_item not in my_inventory:
            return False
        
        if their_item not in friends_inventory:
            return False

        my_inventory.remove(my_item)
        friends_inventory.remove(their_item)

        my_inventory.append(their_item)
        friends_inventory.append(my_item)

        return True
                        

    def swap_first_item(self,friend):
        my_inventory=self.inventory
        friends_inventory=friend.inventory

        if my_inventory==[]:
            return False
        
        if friends_inventory==[]:
            return False   

        my_first_item=my_inventory[0]  
        friends_first_item=friends_inventory[0]  

        my_inventory.remove(my_first_item)
        friends_inventory.remove(friends_first_item)  

        my_inventory.append(friends_first_item)
        friends_inventory.append(my_first_item) 
        return True             



        