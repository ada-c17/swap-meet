from swap_meet.item import Item
# '''wave1:We made a class named vendor andeach vendor will have an attribute named inventory which is a list and is optional'''
class Vendor:
    def __init__(self,  inventory = None):
        if inventory is None:
            self.inventory=[]
        else:
            self.inventory=inventory

# '''wave1:instance method for adding item to inventory'''
    def add (self,item):
        self. inventory.append(item)
        return item
    # '''wave1:instance method for removing item from inventory. if item not in inventory return False'''
    def remove(self,item):
        if item in self.inventory:
           self. inventory.remove(item)
           return item
        else:
            return False
    #wave 2: composition with item.py: get-by_category is an instance method . it takes a category which is a string and returns list of items in inventory with that category
    def get_by_category(self,category):
        items=[]
        for item in self.inventory:
           if category==item.category:
              items.append(item)
        return items
    #wave3:swap_items:instance method:if my item in my inventory and their item in friend inventory swap them. Otherwise if one of us do not have that return False
    def swap_items (self,friend,my_item,their_item):
        if my_item in self.inventory and their_item in friend.inventory:

                self.remove(my_item)
                self.add(their_item)
                friend.remove(their_item)
                friend.add(my_item)
                return True
        else:
            return False
    #wave 4: swap_first_item:swap first item of vendor and friends inventory list and return True. If any of the two has an empty list return False
    def swap_first_item(self,friend):
        
        if len(self.inventory)==0 or len(friend.inventory)==0:
            return False
        my_first = self.inventory[0]
        friend_first = friend.inventory[0]
        result=self.swap_items (friend,my_first,friend_first)
        return True
       
    #wave 6: takes in a category and looks for the item in inventory in same category and return the item with higher condition if it finds return it. else returns None.
    def get_best_by_category(self,category):
        max_condition=0
        best_item=None
        for item in self.inventory:
            if item.category==category:
                if item.condition>max_condition:
                    max_condition=item.condition
                    best_item=item
        return best_item
        
    #wave 6: swap best by category will check if my inventory has any item in category of their priority and if their inventory has any item in category of my priority and it will swap the highest condition it finds. and return True if it cant find the item of the mentioned category in my inventory or friends inventory it will jusr return None
    def swap_best_by_category(self,other,my_priority,their_priority):
        
        their_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
       
        if their_best == None or my_best == None:
            return False
        else:
            self.swap_items(other,my_best,their_best)
            return True


        












