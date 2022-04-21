from .item import Item


class Vendor:
    def __init__(self, inventory=None):
        
        self.inventory = inventory if inventory else []
        

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
        
    def get_by_category(self, category_name):
        category_items=[item for item in self.inventory if item.name == category_name]
        return category_items
    def swap_items(self, another_vendor, my_item, their_item):
        
        if my_item not in self.inventory or their_item not in another_vendor.inventory:
            return False
        self.remove(my_item)
        self.add(their_item)
        another_vendor.add(my_item)
        another_vendor.remove(their_item)
        return True

    def swap_first_item(self, another_vendor):
        
        # if not self.inventory or not another_vendor.inventory:
        #     return False
        # my_item = self.inventory[0]
        # their_item = another_vendor.inventory[0]
        # self.swap_items(another_vendor, my_item, their_item)
        self.inventory[0], another_vendor.inventory[0] = another_vendor.inventory[0], self.inventory[0]
        return True

    def get_best_by_category(self, target_category):
        if not self.inventory:
            return None
        item_matching_category=self.get_by_category(target_category)
        if not item_matching_category:
            return None
        condition=-1
        best_item=None
        for item in item_matching_category:
            if item.condition>condition:
                best_item=item
                condition=item.condition
        return best_item
        # flag = False
        # counter = -1
        # for item in self.inventory:
        #     if item.category == target_category:
        #         flag = True
        #         if item.condition > counter:  # return the first item if there is a tie
        #             res = item
        #             counter=item.condition
        # if not flag:
        #     return None
        # return res


        # res=None
        # counter=-1
        # for item in self.inventory:
        #     if item.category == target_category:
                
        #         if item.condition > counter:  # return the first item if there is a tie
        #             res = item
        #             counter = item.condition
        # return res
    def swap_best_by_category(self, other, my_priority, their_priority):
        
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)
        if not my_item or not their_item:
            return False
        self.swap_items(other, my_item, their_item)
        return True
