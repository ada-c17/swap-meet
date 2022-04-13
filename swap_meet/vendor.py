class Vendor:
    def __init__(self, inventory=None):  #define class 
        if not inventory:               #return empty list, if none
            self.inventory = []         #attribute set-up

        else:
            self.inventory = inventory   #if inv data present
        
    def add(self, item):                  # a instance method
        self.inventory.append(item)
        return item

    def remove(self, item): 
        if item in self.inventory:
            self.inventory.remove(item)
            return item    
            
        else:   
            return False 
            
                #a instance method
    def get_by_category(self, cat_name):
        cat_list = []
        for item in self.inventory:
            if item.category == cat_name:
                cat_list.append(item)
        return  cat_list     
        
    def swap_items(self, friend, my_item, friend_item):
        if my_item in self.inventory and friend_item in friend.inventory:
            friend.inventory.append(my_item)
            self.inventory.append(friend_item)
            friend.inventory.remove(friend_item)
            self.inventory.remove(my_item)
            return True
        return False

    def swap_first_item(self, friend):
        if not self.inventory or not friend.inventory:
            return False
        else:
            
            self.inventory.append(friend.inventory[0])
            friend.inventory.append(self.inventory[0])

            self.inventory.remove(self.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            return True

    def get_best_by_category(self, category):
        if not self.inventory:
            return None
        else:
            items = self.get_by_category(category)
            if items: return max( items, key=lambda item: item.condition )

        

    def swap_best_by_category(self, other, my_priority, their_priority):


        friend_swap = other.get_best_by_category(my_priority)
        my_swap = self.get_best_by_category(their_priority)

        if not friend_swap:
            return False
        if not my_swap:
            return False    
        
        self.swap_items(other, my_swap, friend_swap)
        return True
        
        
        # if their_priority not in self.inventory:
        #     return False
        # elif my_priority not in other.inventory:
        #     return False
            
        

        
