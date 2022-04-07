class Vendor:
    def __init__(self, inventory = None):
        if inventory:
            self.inventory = inventory
        else:
            self.inventory = []

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        items_list = []
        for item in self.inventory:
            if item.category == category:
                items_list.append(item)
        return items_list

    def swap_items(self, vendor, my_item, their_item):
            if my_item not in self.inventory or their_item not in vendor.inventory:
                return False
            self.remove(my_item)
            vendor.remove(their_item)
            vendor.add(my_item)
            self.add(their_item)
        
            return True

    def swap_first_item(self, vendor):
            if len(self.inventory) == 0 or len(vendor.inventory) == 0:
                return False
            my_item = self.inventory[0]
            friend_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, friend_item)
            
            return True

    def get_best_by_category(self, category):
        category_list = [
            i for i in self.inventory if i.category == category
        ]
        best_condition = -1
        best_item = None
        for item in category_list:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(
        self,
        other, # Vendor object
        my_priority, # category string
        their_priority # category string
    ):    
        their_priority_exists = False
        for item in self.inventory:
            if item.category == their_priority:
                their_priority_exists = True
                break

        my_priority_exists = False 
        for item in other.inventory:
            if item.category == my_priority:
                my_priority_exists = True
                break

        if not my_priority_exists or not their_priority_exists:
            return False

        get_best_my = self.get_best_by_category(their_priority)
        get_best_other = other.get_best_by_category(my_priority)

        self.swap_items(other, get_best_my, get_best_other)
        return True
