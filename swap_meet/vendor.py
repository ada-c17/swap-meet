
class Vendor:
    def __init__(self, inventory= None):
        inventory = inventory if inventory is not None else []
        self.inventory = inventory


    def add(self, item): 
        self.inventory.append(item)
        return item

    def remove(self, item_to_remove):
        if not self.inventory:
            return False
        elif item_to_remove in self.inventory:
            item_index = self.inventory.index(item_to_remove)
            popped_item = self.inventory.pop(item_index)
            return popped_item
        else:

            return False

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.category == category:
                category_list.append(item)   
        return category_list

    def swap_items(self, Vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in Vendor.inventory:
            return False
        else:
            Vendor.inventory.append(self.remove(my_item))  
            self.inventory.append(Vendor.remove(their_item)) 
            return True

    def swap_first_item(self, Vendor):
        if not Vendor.inventory or not self.inventory:
            return False
        else:
            ven_inventory = Vendor.inventory[0]
            self_inventory = self.inventory[0]
            Vendor.inventory.append(self.remove(self_inventory))
            self.inventory.append(Vendor.remove(ven_inventory)) 
            return True

#             In Wave 6 we will write two methods, `get_best_by_category` and `swap_best_by_category`.

# - `Vendor`s have a method named `get_best_by_category`, which will get the item with the best condition in a certain category
#   - It takes one argument: a string that represents a category
#   - This method looks through the instance's `inventory` for the item with the highest `condition` and matching `category`
#     - It returns this item
#     - If there are no items in the `inventory` that match the category, it returns `None`
#     - It returns a single item even if there are duplicates (two or more of the same item with the same condition)



    def get_best_by_category(self, category):
        categorized_list= self.get_by_category(category)
        if not categorized_list:
            return None
        best_condition = categorized_list[0]
        for item in categorized_list:
            if item.condition > best_condition.condition:
                best_condition = item
        return best_condition 

            # 
# - `Vendor`s have a method named `swap_best_by_category`, which will swap the best item of certain categories with another `Vendor`
#   - It takes in three arguments
#     - `other`, which represents another `Vendor` instance to trade with
#     - `my_priority`, which represents a category that the `Vendor` wants to receive
#     - `their_priority`, which represents a category that `other` wants to receive
#   - The best item in my inventory that matches `their_priority` category is swapped with the best item in `other`'s inventory that matches `my_priority`
#     - It returns `True`
#     - If the `Vendor` has no item that matches `their_priority` category, swapping does not happen, and it returns `False`
#     - If `other` has no item that matches `my_priority` category, swapping does not happen, and it returns `False`
    def swap_best_by_category(self, other, my_priority, their_priority):
        vendors_best= other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        if not vendors_best or not my_best:
            return False
        else:
            self.swap_items(other, my_best, vendors_best)
            return True


      