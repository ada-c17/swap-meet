class Vendor:
        def __init__(self, inventory = None):
            if not inventory:
                inventory = []
            self.inventory = inventory

        def add(self, item):
            if not item in self.inventory:
                self.inventory.append(item)
                return item

        def remove(self, item):
            if item in self.inventory:
                self.inventory.remove(item)
                return item
            else:
                return False
        
        def get_by_category(self, category):
            item_list = []
            for item in self.inventory:
                if category == item.category:
                    item_list.append(item)
            return item_list

        def swap_items(self, vendor, my_item, their_item):
            if my_item not in self.inventory or their_item not in vendor.inventory:
                return False
            self.inventory.remove(my_item)
            vendor.remove(their_item)
            self.inventory.append(their_item)
            vendor.inventory.append(my_item)

            return True
        def swap_first_item(self, vendor):
            if len(self.inventory) == 0 or len(vendor.inventory) == 0:
                return False
            # Get first item from inventory
            first_item_inventory = self.inventory[0]
            # Get first item from their inventory
            first_item_vendor = vendor.inventory[0]
            # Remove first item from inventory 
            self.inventory.remove(first_item_inventory)
            vendor.inventory.remove(first_item_vendor)
            # "Update" first item on their inventory 
            vendor.inventory.insert(0, first_item_inventory)
            self.inventory.insert(0,first_item_vendor )
            
            
            return True
        
        def get_best_by_category(self, category):
            highest_item = None
            higest_condition = 0
            all_items = []
            category = self.get_by_category(category)

            if not category:
                return None
            

            best_item = category[0]

            for item in category:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
        
        def swap_best_by_category(self, other, my_priority, their_priority):
            my_item = self.get_best_by_category(their_priority)
            their_item = other.get_best_by_category(my_priority)
            if not my_item or not their_item:
                return False
            
            self.swap_items(other, my_item, their_item)
            return True




