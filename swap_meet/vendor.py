from operator import itemgetter


class Vendor:

    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
        except ValueError:
            return False
        return item
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.category == category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, vendor, my_item, their_item):
        #this if calls .remove regardless of outcome;
        #will cause item removal if present in inventory
        if not (vendor.remove(their_item)):
            return False
        if not (self.remove(my_item)):
            vendor.add(their_item)
            return False

        vendor.add(my_item)
        self.add(their_item)
        return True
    
    def swap_first_item(self, vendor):
        if len(self.inventory) < 1 or len(vendor.inventory) < 1:
            return False
        vendor.add(self.inventory[0])
        self.remove(self.inventory[0])
        self.add(vendor.inventory[0])
        vendor.remove(vendor.inventory[0])
        return True
    
    def get_best_by_category(self, category):
        item_list = self.get_by_category(category)
        
        if item_list:
            best_item = item_list[0]
            for item in item_list:
                if item.condition > best_item.condition:
                    best_item = item
        else:
            return None

        return best_item