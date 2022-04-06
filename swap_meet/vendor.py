class Vendor:
    def __init__(self, inventory =[]):
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
        

    def get_by_category (self, category):   
        same_category = []
        for item in self.inventory:
            if category == item.category:
                same_category.append(item)
            
        return same_category


    def swap_items(self, other_vendor, self_item, other_vendor_item):
        if other_vendor_item in other_vendor.inventory and self_item in self.inventory:
            self.remove(self_item)
            other_vendor.remove(other_vendor_item)
            self.add (other_vendor_item)
            other_vendor.add(self_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory)>= 1 <=len(other_vendor.inventory):
            swap_first = self.swap_items(other_vendor, self.inventory[0],other_vendor.inventory[0])
            return swap_first
        return False

    def get_best_by_category(self, category):
        highest = 0
        best_item = None
        if len(self.inventory) != 0:
            for item in self.inventory:
                if item.category == category and item.condition > highest:
                    highest = item.condition
                    best_item = item

        return best_item


    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best!=None and their_best != None:
            the_swap = self.swap_items(other, my_best, their_best)
            return True
        else: 
            return False    