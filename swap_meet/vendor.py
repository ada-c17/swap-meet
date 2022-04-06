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
            return False  

    def get_by_category(self, category):
        
        items = [] #creating a list where i am going to store all my objects with selected category
        for i in self.inventory:
            if category==i.category:
                items.append(i)
        return items
       
    def swap_items(self,friend,my_item,their_item):
       
        if my_item not in self.inventory or their_item not in friend.inventory:# checking if items are in inventories
            return False

        self.remove(my_item) #  if my item is in my inventory it will be removed from there and added to my friend's inventory
        friend.remove(their_item) 

        self.add(their_item) #removed item from friend's inventory is added to my inventory
        friend.add(my_item)

        return True

    def swap_first_item(self,friend):
        if self.inventory==[] or friend.inventory==[]: #checking if inventory is empty
            return False  

        my_first_item=self.inventory[0]   #first item in my inventory 
        friends_first_item=friend.inventory[0]  #first item in friend's inventory

        self.remove(my_first_item) # removing first object from my inventory 
        friend.remove(friends_first_item)  

        self.add(friends_first_item) # adding first object in friend's inventory to my inventory
        friend.add(my_first_item) 
        return True    

    def get_best_by_category(self, category):
        matching_category_item_list=[] # list to store all the objects with specific category

        for i in self.inventory: # iterating over each object in inventory 
            if category==i.category: # checking if the category is equal to category in inventory
                matching_category_item_list.append(i) # add that object with matching category to the list 

        if len(matching_category_item_list) == 0: 
            return None
        
        best_item_in_category=matching_category_item_list[0] # the best item in a list will be first item 
       
        for e in matching_category_item_list: # iterate over each object in a list to check
            if e.condition>best_item_in_category.condition: # comparing each object's condition in a list 
                best_item_in_category = e # the one that is bigger becomes the best

        return best_item_in_category

    def swap_best_by_category(self,other,my_priority,their_priority):
        what_I_want = other.get_best_by_category(my_priority)
        what_they_want = self.get_best_by_category(their_priority)

        return self.swap_items(other, what_they_want, what_I_want) #to reduce the amount of code i am using swap_items method that has the same logic

    #Bonus
    def get_newest_item(self): # looking for the newest item in the inventory : the one with smallest age

        sorted_inventory=self.inventory # decided to sort the inventory and the first element will be with smallest age
        sorted_inventory.sort(key=lambda x:x.age)  #could not do smth like: self.inventory.sort() and found similar example in internet how to sort objects by parameter
        
        newest_item=sorted_inventory[0] # newest item is the first item in a list
        if newest_item.age==0:
            return False
        return newest_item

    def swap_by_newest(self,other):
        
        my_newest=self.get_newest_item()
        friends_newest=other.get_newest_item()

        return self.swap_items(other,my_newest,friends_newest)  # the same logic as in swap_items that is why i desided to use it here 



        