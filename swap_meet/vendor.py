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

    def swap_first_item(self, friend_vendor):
        # my_first_item = self.inventory[0]
        # their_first_item = friend_vendor.inventory[0]
        # self.inventory.append(their_first_item)
        # self.inventory.remove(my_first_item)
        # friend_vendor.inventory.append(my_first_item)
        # friend_vendor.inventory.remove(their_first_item)
        # return True
        if self.inventory == [] or friend_vendor.inventory == []:
            return False
        else:
            self.swap_items(friend_vendor, self.inventory[0], friend_vendor.inventory[0])
            return True