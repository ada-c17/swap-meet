
class Vendor:

    # Creator: Each Vendor object has an attribute inventory
    # The inventory should be empty if the caller does not
    # provide any argument.
    def __init__(self, inventory=None):
        # If the caller did not provide an inventory,
        # then create a new empty list and save in the new
        # Vendor's object inventory
        if not inventory:
            self.inventory = []
        else:
            self.inventory = inventory

    # method: add item to inventory
    # the argument item is a reference to an object of class Item
    def add(self, item):
        self.inventory.append(item)
        return item

    # method: remove item from inventory
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False
    # test_wave_02
    # method: create a list of item by category
    def get_by_category(self, category):
        list_item_by_category= []
        for item in self.inventory:
            if item.category == category:
                list_item_by_category.append(item)
        return list_item_by_category

    # test_wave_03
    # if my_item not in self_inventory and their_item not in vendor_inventory
    # do not swap
    def swap_items(self,vendor, my_item,their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        self.remove(my_item)
        vendor.add(my_item)
        vendor.remove(their_item)
        self.add(their_item)
        return True
    #test-wave_04
    def swap_first_item(self, vendor):
        # removes the first item in self.inventory and add to vendor inventory
        # removes the first item from friend inventory and add to self inventory
        # return True
        # if either self or friend has empty inventory, return False
        
        if not self.inventory or not vendor.inventory:
            return False
        first_item_in_self = self.inventory[0]
        first_item_in_vendor = vendor.inventory[0]
        self.remove(first_item_in_self)
        vendor.remove(first_item_in_vendor)
        vendor.add(first_item_in_self)
        self.add(first_item_in_vendor)
        return True
    #___testwave _06
    #input: one argument(string) that represents a category
    #output: get the item with the best condition in a certain category
    def get_best_by_category(self, category):
        my_cat_list = []
        for item in self.inventory:
            if item.category == category:
                my_cat_list.append(item)
        
        if len(my_cat_list) == 0:
            return None

        highest_score_item = my_cat_list[0]
        for item in my_cat_list:
            if item.condition > highest_score_item.condition:
                highest_score_item = item
        return highest_score_item
    #---------------
    '''
    swap_best_by_category: swap the best item of certain categories with another vendor
    inputs:
        other : the other vendor
        my_priority : a category that the Vendor wants to receive
        their_priority: a category that other wants to receive
    outputs: to swap
        return True - vendor's best item must match their priority and
        the other 's best item must match the vendor my priority
        return False - if vendor best item not match their_priority category
        return False - if other has no item that match my_priority
    '''
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            return self.swap_items(other,my_best_item,their_best_item)
        else:
            return False


        # my_best_item = self.get_best_by_category(their_priority)
        # their_best_item = other.get_best_by_category(my_priority)
        # if my_best_item and their_best_item:
        #     self.remove(my_best_item)
        #     other.remove(their_best_item)
        #     self.add(their_best_item)
        #     other.add(my_best_item)
        #     return True
        # else:
        #     return False


    
        
        
    
    