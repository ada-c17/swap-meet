class Vendor:
    def __init__(self, inventory = None):
        if not inventory:
            inventory = []
        self.inventory = inventory

    def add(self, add_item):
        add = self.inventory.append(add_item)
        return add_item

    def remove(self, sub_item):
        if sub_item in self.inventory:
            self.inventory.remove(sub_item)
            return sub_item
        else:
            return False
    

    def get_by_category(self, category):
        each_category = []
        for item in self.inventory:
            if item.category == category:
                each_category.append(item)
        return each_category


    def swap_items(self, friend_vendor, my_item, their_item):
        if my_item not in self.inventory\
        or their_item not in friend_vendor.inventory:
            return False
        else:
            self.remove(my_item)
            self.add(their_item)
            friend_vendor.remove(their_item)
            friend_vendor.add(my_item)
            return True
        

    def swap_first_item(self, new_vendor):
        if self.inventory == [] or new_vendor.inventory == []:
            return False
        else:
            self.add(new_vendor.inventory[0])
            new_vendor.add(self.inventory[0])
            self.remove(self.inventory[0])
            new_vendor.remove(new_vendor.inventory[0])
            return True



        
        


