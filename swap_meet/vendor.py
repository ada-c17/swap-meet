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

    def get_best_by_category(self, category):
        matching_category_item_list=[]

        for i in self.inventory:
            if category==i.category:
                matching_category_item_list.append(i)

        if len(matching_category_item_list) == 0:
            return None
        
        best_item_in_category=matching_category_item_list[0]
       
        for e in matching_category_item_list:
            if e.condition>best_item_in_category.condition:
                best_item_in_category = e

        return best_item_in_category

    def swap_best_by_category(self,other,my_priority,their_priority):
        what_I_want = other.get_best_by_category(my_priority)
        what_they_want = self.get_best_by_category(their_priority)

        return self.swap_items(other, what_they_want, what_I_want) #to reduce the amount of code i am using swap_items method that has the same logic

    #Bonus
    def get_newest_item(self):


        sorted_inventory=self.inventory
        sorted_inventory.sort(key=lambda x:x.age) 
        
        newest_item=sorted_inventory[0]
        if newest_item.age==0:
            return False
        return newest_item

    def swap_by_newest(self,other):
        
        my_newest=self.get_newest_item()
        friends_newest=other.get_newest_item()

        return self.swap_items(other,my_newest,friends_newest)   



        