
class Vendor:
    def __init__(self, inventory=None):
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
        else:
            return False
    
    def get_by_category(self, category):
        items = []
        for item in self.inventory:
            if item.category == category:
                items.append(item)
        return items
    
    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False

        self.inventory.remove(my_item)
        vendor_friend.inventory.remove(their_item)
        if their_item.category not in self.inventory:
            self.inventory.append(their_item)
            vendor_friend.inventory.append(my_item)
        return True
# It removes the my_item from this Vendor's inventory, and adds it to the friend's inventory
# It removes the their_item from the other Vendor's inventory, and adds it to this Vendor's inventory
# It returns True
# If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain 
# their_item, the method returns False


