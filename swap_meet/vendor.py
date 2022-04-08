class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, add_item):
        add = self.inventory.append(add_item)
        return add_item

    def remove(self, sub_item):
        if sub_item in self.inventory:
            self.inventory.remove(sub_item)
            return sub_item
        else:
            return False
    

    def get_by_category(self, category):
        each_category = []
        for item in self.inventory:
            if item.category == category:
                each_category.append(item)
        return each_category


    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory\
        or their_item not in friend_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.remove(their_item)
            friend_vendor.add(my_item)
            return True
        

    def swap_first_item(self, new_vendor):
        if self.inventory == [] or new_vendor.inventory == []:
            return False
        else:
            self.add(new_vendor.inventory[0])
            new_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            new_vendor.remove(new_vendor.inventory[0])
            return True



    def get_best_by_category(self, best_category):
        #iterate through instances inventory (self.inventory)
        
        best_item = None
        highest_condition = 0
        for item in self.inventory:
            if item.category == best_category:
                if item.condition > highest_condition:
                    highest_condition = item.condition
                    best_item = item
            
        return best_item
            


    def swap_best_by_category(self, other, my_priority, their_priority):
        my_swap = self.get_best_by_category(their_priority)
        their_swap = other.get_best_by_category(my_priority)
        swap_result = self.swap_items(other, my_swap, their_swap)
        return swap_result
        



        
        


