from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory = None):
            if not inventory:
                inventory = []
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
            my_item = self.inventory[0]
            their_item = vendor_friend.inventory[0]
            self.swap_items(vendor_friend, my_item, their_item)
            return True

    def get_best_by_category(self, category):

        category_items = self.get_by_category(category)

        if category_items == []:
            return None
        
        else:
            best_item = category_items[0]
            for item in category_items:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_product = self.get_best_by_category(their_priority)
        their_product = other.get_best_by_category(my_priority)
        self.swap_items(other, my_product, their_product)
        if my_product == None or their_product == None:
            return False

        return True

