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
    
    def get_by_category(self, category):
        same_catagory_items = []
        for item in self.inventory:
            if item.category == category:
                same_catagory_items.append(item)
        return same_catagory_items


    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory:
            return False
        elif their_item not in friend_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.remove(their_item)
            friend_vendor.add(my_item)
        return self.inventory 
        
