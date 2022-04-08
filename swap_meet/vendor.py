from swap_meet.item import Item
class Vendor:

    def __init__ (self, inventory=None):
       self.inventory = inventory
       if inventory is None:
           self.inventory = []


  

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else :
             self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items = []
        for item in self.inventory:

            if item.category == category:
                items.append(item)
        return items

          


    def swap_items(self,vendor, my_item, their_item ):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        vendor.inventory.append(my_item)
        vendor.inventory.remove(their_item)
        if my_item in vendor.inventory and their_item in self.inventory:
            return True
        else:
            return False    

    def swap_first_item(self,vendor):
        if vendor.inventory == []:
            return False
        else:
            if self.inventory == []:
                return False
            self.inventory.append(vendor.inventory[0])
            vendor.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
            vendor.inventory.remove(vendor.inventory[0])
        return True

    def get_best_by_category(self, category):    
        best_item = None
        best_condition = 0
        for item in self.inventory:
            if item.category == category:
                if item.condition > best_condition:
                    best_item = item
                    best_condition = item.condition
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        if my_best == None:
            return False
        their_best = other.get_best_by_category(my_priority)
        if their_best == None:
            return False
        return self.swap_items(other, my_best, their_best) 
        


        







        