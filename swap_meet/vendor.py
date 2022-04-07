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


    def get_by_category(self, category):
        inventory_by_category = [] 
        for item in self.inventory:
            if item.category == category:
                inventory_by_category.append(item)
        return inventory_by_category
            
                
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.add(my_item)
            self.remove(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            return True 
        return False 
    

    def swap_first_item(self, other_vendor):
        try:
            my_item = self.inventory[0]
            their_item = other_vendor.inventory[0]
            first_items = self.swap_items(other_vendor, my_item, their_item)
            return first_items
        except IndexError:
            return False 


    def get_best_by_category(self, category):
        max_condition = 0
        max_item = None 
        for item in self.inventory:
            if item.condition > max_condition and item.category == category:
                max_condition = item.condition  
                max_item = item
        return max_item 


    def swap_best_by_category(self, other, my_priority, their_priority):
        their_item = self.get_best_by_category(their_priority)
        my_item = other.get_best_by_category(my_priority)
        return self.swap_items(other, their_item, my_item)



            
            
    
        
                
        
        
        


        



        



