class Vendor:
    '''
    The Vendor class represents instances of vendors collecting, removing, filtering,
    and swapping items with other vendors. Instances of vendors can collect items
    in the inventory attribute. Inventory is a list that instances of Vendors
    can populate with instances of the Item class in item.py.
    '''

    def __init__(self, inventory = None):
        if not inventory:
           inventory = []
        self.inventory = inventory

    def add(self, item):
        '''
        Input: item
        Output: item
        Adds one item to the class' inventory list.
        Returns False if item is invalid.
        '''

        if not item:
            return False

        self.inventory.append(item)
        return item

    def remove(self, item):
        '''
        Input: item
        Output: item
        Removes one item from the class' inventory list.
        Returns False if input is not in inventory.
        '''

        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        '''
        Input: category (string)
        Output: list_of_items_per_cat (list)
        Returns a list of items with input category.
        '''

        list_of_items_per_cat = [item for item in self.inventory if item.category == category]
        return list_of_items_per_cat

    def swap_items(self, other_vendor, my_item, their_item):
        '''
        Input: other_vendor (instance of Vendor class), my_item, their_item
        Output: True (boolean)
        Removes my_item from self.inventory (this class' inventory).
        Removes their_item from other_vendor.inventory.
        Adds my_item to other_vendor.inventory.
        Adds their_item to self.inventory.
        Returns False if my_item or their_item
        are not in respective inventories.
        '''

        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        other_vendor.add(my_item)
        self.remove(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)

        return True

    def swap_first_item(self, other_vendor):
        '''
        Input: other_vendor (instance of Vendor class), my_item, their_item
        Output: True (boolean)
        Makes use of the swap_items instance method to swap the first element in
        each vendor's respective inventory.
        Returns False if either inventory is empty.
        '''

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True

    def get_best_by_category(self, category):
        '''
        Input: category (string)
        Output: best_item (the item with the highest condition attribute
        within input category)
        Returns the item with the highest condition in the input category.
        Makes use of the get_by_category instance method to create a
        list of elements whose category values match the input.
        This list is stored in the variable items_by_cat.
        Returns False if there are no items in preferred category.
        '''

        items_by_cat = self.get_by_category(category)

        if len(items_by_cat) == 0:
            return None

        best_item = items_by_cat[0]
        for item in items_by_cat:
            if item.condition > best_item.condition:
                best_item = item

        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        '''
        Input: other, my_priority, their_priority
        Output: True (boolean)
        1. Makes use of the get_best_by_category instance method to:
        find the item of the other vendor's priority category in the best
        condition in one's own inventory, and viceversa.
        2. Swaps said preferred-category "best" items between vendors.
        Return False if such items do not exist (aka if priority category
        does not exist in their collection)
        '''

        best_item_other = other.get_best_by_category(my_priority)
        best_item_mine = self.get_best_by_category(their_priority)

        if not best_item_other or not best_item_mine:
            return False

        self.swap_items(other, best_item_mine, best_item_other)

        return True
