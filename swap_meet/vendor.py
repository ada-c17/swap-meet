from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category = ""):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor_friend, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor_friend.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            vendor_friend.inventory.append(my_item)
            vendor_friend.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
    
    def swap_first_item (self, vendor_friend):
        if self.inventory == [] or vendor_friend.inventory == []:
            return False
        else:
            my_item = self.inventory.pop(0)
            vendor_friend.inventory.append(my_item)
            
            their_item = vendor_friend.inventory.pop(0)
            self.inventory.append(their_item)
            return True



