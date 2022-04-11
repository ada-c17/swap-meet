
class Vendor:
    def __init__(self, inventory= None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory


    def add(self, item): 
        self.inventory.append(item)
        return item

    def remove(self, item_to_remove):
        if not self.inventory:
            return False
        elif item_to_remove in self.inventory:
            item_index = self.inventory.index(item_to_remove)
            popped_item = self.inventory.pop(item_index)
            return popped_item
        else:
            return False

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)   
        return category_list

    def swap_items(self, Vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in Vendor.inventory:
            return False
        else:
            Vendor.inventory.append(self.remove(my_item))  
            self.inventory.append(Vendor.remove(their_item)) 
            return True

    def swap_first_item(self, Vendor):
        if not Vendor.inventory or not self.inventory:
            return False
        else:
            self.swap_items(Vendor, self.inventory[0], Vendor.inventory[0])
            return True

    """Refactored Swap_first_item() post Swap Meet  Wrap up 
    def swap_first_item(self, Vendor):
        if not Vendor.inventory or not self.inventory:
            return False
        else:
            ven_inventory = Vendor.inventory[0]
            self_inventory = self.inventory[0]
            Vendor.inventory.append(self.remove(self_inventory))
            self.inventory.append(Vendor.remove(ven_inventory)) 
            return True"""
            

    def get_best_by_category(self, category):
        categorized_list= self.get_by_category(category)
        if not categorized_list:
            return None
        best_condition = categorized_list[0]
        for item in categorized_list:
            if item.condition > best_condition.condition:
                best_condition = item
        return best_condition 


    def swap_best_by_category(self, other, my_priority, their_priority):
        vendors_best= other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not vendors_best or not my_best:
            return False
        else:
            self.swap_items(other, my_best, vendors_best)
            return True


      