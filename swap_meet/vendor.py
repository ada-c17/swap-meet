# Wave 1 
class Vendor:
    def __init__(self, inventory=[]):
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

    # Wave 2
    def get_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        return items

    # Wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True
    
    # Wave 4
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0: 
            return False

        vendor_first_item = self.inventory[0]
        friend_first_item = other_vendor.inventory[0]

        self.remove(vendor_first_item)
        self.add(friend_first_item)

        other_vendor.remove(friend_first_item)
        other_vendor.add(vendor_first_item)

        return True

