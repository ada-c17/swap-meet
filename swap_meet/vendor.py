class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self,*items):
        if not items:
            return None
        for item in items:
            self.inventory.append(item)
        return items[0] if len(items) == 1 else items
    
    def remove(self,*items):
        if not items:
            return None
        for item in items:
            if item not in self.inventory:
                return False
            self.inventory.remove(item)
        return items[0] if len(items) == 1 else items
    
    def get_by_category(self,category):
        return [item for item in self.inventory 
                    if item.category == category]
    
    def swap_items(self,other_vendor,current_item,exchange_item):
        if (current_item not in self.inventory or
            exchange_item not in other_vendor.inventory):
            return False
        handoff = self.remove(current_item),other_vendor.remove(exchange_item)
        self.add(handoff[1])
        other_vendor.add(handoff[0])
        return True
    
    def swap_first_item(self,other_vendor):
        if (not self.inventory or 
            not other_vendor.inventory):
            return False
        return self.swap_items(other_vendor,self.inventory[0],other_vendor.inventory[0])
    
    def get_best_by_category(self,category):
        items = self.get_by_category(category)
        if len(items) == 0:
            return None
        ratings = [item.condition for item in items]
        return items[ratings.index(max(ratings))]
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        own_item = self.get_best_by_category(their_priority)
        swap_item = other.get_best_by_category(my_priority)
        
        if not (own_item and swap_item):
            return False
        return self.swap_items(other,own_item,swap_item)