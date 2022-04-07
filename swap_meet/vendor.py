from swap_meet.item import Item

class Vendor:

    def __init__(self, inventory = None):
        """
        Vender attribute named 'inventory' which is an empty list by default

        Optional to pass in list with the keyword argument 'inventory'
        """


        if inventory is None:
            inventory = []

        self.inventory = inventory


    def add(self, item_to_add):
        """
        Input: one item to add to inventory (string)

        Output: return item that was added (string)
        """
        self.inventory.append(item_to_add)

        return item_to_add


    def remove(self, item_to_remove):
        """
        Input: one item to remove from the inventory (string)

        Output: return item that was removed (string)
        """

        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False


    def get_by_category(self, category=""):
        """
        Input: empty string as default or some string

        Output: list of items ['Computer', 'Calculator']
        """
        found_items = []

        for ele in self.inventory:
            # Loop through the inventory list in Vendor
            if category == ele.category:
                # If the category input string matches the inventory 
                # list element's category, add to list of 'found items'
                found_items.append(ele)

        return found_items


    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Input: 
            1. 'friend_vendor': another instance of Vendor to swap Items with
            2. 'my_item': item to swap from this Vendor's inventory
            3. 'their_item': item to swap from friend's inventory

        Output: 
            1. Return True if swap is successful. 
            2. Otherwise, return False
        """
        
        if (my_item in self.inventory) and (their_item in friend_vendor.inventory):
            # Remove item from this Vendor's inventory
            self.remove(my_item)
            # # Add to friend's inventory
            friend_vendor.add(my_item)

            # Remove item from friend's inventory
            friend_vendor.remove(their_item)
            # Add item to this Vendor's inventory
            self.add(their_item)

            return True
        else:
            return False


    def swap_first_item(self, vendor_friend):
        """
        Input: vendor_friend: friend that this Vendor is swapping with

        Output: 
            1. Return True if swap is successful.
            2. Return False if either inventories are empty.
        """

        if (len(self.inventory) == 0) or (len(vendor_friend.inventory) == 0):
            # If the Vendor or the friend have empty inventories, return False
            return False
        else:
            # Consider the first item in this Vendor's inventory and vendor_friend's inventory
            # Remove the first item from this Vendor's inventory, add it to vendor_friend's inventory
            # Remove the first item from the friend's inventory, add it to this Vendor's inventory
            # Return True when the swap is done
            my_first_item = self.inventory[0]
            their_first_item = vendor_friend.inventory[0]

            self.inventory[0] = their_first_item
            vendor_friend.inventory[0] = my_first_item

            return True
    

    def get_best_by_category(self, best_category):
        # Function will get the item with the best condition in a certain category

        # Look through the instance's 'inventory' for the item with 
        # The highest 'condition' and matching 'category'

        """
        Input: 'item_category': string representing category

        Output: 
            1. Item that matches the category
            2. If no match, return None
        
            Return a single item even if there's duplicates
        """
        category_items = self.get_by_category(best_category)

        if not category_items:
            return None

        best_item = category_items[0]

        for product in category_items:
            if product.condition >= best_item.condition:
                best_item = product

        return best_item
        


    def swap_best_by_category(self, other, my_priority, their_priority):

        """
        Input: 
            1. 'other': another 'Vendor' to trade with
            2. 'my_priority': category that the 'Vendor' wants to receive
            3. 'their_priority': category that 'other' wants to receive
        
        Output:
            1. Return True if best item in my inventory matches 'their_priority' is swapped
                with the best item in 'other's inventory that matches 'my_priority'
            2. Return False if item priorities don't match and swap doesn't happen
        """
        
        # Category the Vendor wants to receive
        my_best_item_to_swap = self.get_best_by_category(their_priority)
        # Category the other Vendor wants to receive
        their_best_item_to_swap = other.get_best_by_category(my_priority)
        # Returning the best item in those categories


        swap_the_best = self.swap_items(other, my_best_item_to_swap, their_best_item_to_swap)
        
        return swap_the_best