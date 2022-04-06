class Vendor:

    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        items_in_category = []
        
        for item in self.inventory:
            if category == item.category:
                items_in_category.append(item)
        return items_in_category

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            other_vendor.add(my_item)
            
            other_vendor.remove(their_item)
            self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            my_first_item = self.remove(self.inventory[0])
            other_vendor.add(my_first_item)
            
            thier_first_item = other_vendor.remove(other_vendor.inventory[0])
            self.add(thier_first_item)
        return True




