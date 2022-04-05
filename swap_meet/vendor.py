class Vendor:
    def __init__(self, inventory = None):
        if inventory is None:
            self.inventory = []
        else:
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
        output = [Item for Item in self.inventory if category == Item.category]
        return output

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            other_vendor.add(my_item)
            self.add(their_item)
            other_vendor.remove(their_item)
            self.remove(my_item)
            return True
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            self.add(other_vendor.inventory[0]) 
            other_vendor.add(self.inventory[0])  
            self.remove(self.inventory[0]) 
            other_vendor.remove(other_vendor.inventory[0])
            return True
    
    def get_best_by_category(self, category):  
        try: 
            max_value = max(Item.condition for Item in self.inventory if Item.category == category)
            for Item in self.inventory:
                if Item.category == category and Item.condition == max_value:
                    return Item
        except:
            return None
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_inventory = self.get_by_category(their_priority)
        other_inventory = other.get_by_category(my_priority)
        if len(my_inventory) > 0 and len(other_inventory) > 0:
                self.add(other.get_best_by_category(my_priority))
                other.add(self.get_best_by_category(their_priority))
                self.remove(self.get_best_by_category(their_priority))
                other.remove(other.get_best_by_category(my_priority))
                return True