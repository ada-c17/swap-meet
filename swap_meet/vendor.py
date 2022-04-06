class Vendor:
    def __init__(self, inventory=None):
        
        self.inventory = inventory if inventory is not None else []


    def add(self, item):
        self.inventory.append(item)
        return item


    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False


    def get_by_category(self, category):

        # filter method searches through the inventory and returns a list if the item matches the category
        category_items = list(filter(lambda x: x.category == category, self.inventory))

        # alternative method is using list comprehension
        # category_items = [item for item in self.inventory if item.category == category]

        # without filter or list comprehension
        # category_items = []
        # for item in self.inventory:
        #     if item.category == category:
        #         category_items.append(item)

        return category_items


    def swap_items(self, vendor, my_item, their_item):

        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False

        vendor.add(self.remove(my_item))
        self.add(vendor.remove(their_item))

        return True


    def swap_first_item(self, vendor):

        if not self.inventory or not vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = vendor.inventory[0]
        self.swap_items(vendor, my_item, their_item)

        return True


    def get_best_by_category(self, category):

        items_list = self.get_by_category(category)

        if not items_list:
            return None

        best_item = max(items_list, key = lambda x: x.condition)
       
        # without using max
        # best_condition = 0
        # best_item = None

        # for item in items_list:
        #     if item.condition > best_condition:
        #         best_condition = item.condition
        #         best_item = item

        return best_item


    def swap_best_by_category(self, vendor, my_priority, their_priority):
        
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = vendor.get_best_by_category(my_priority)

        if not my_best_item or not their_best_item:
            return False

        self.swap_items(vendor, my_best_item, their_best_item)

        return True
