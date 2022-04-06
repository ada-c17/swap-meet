from swap_meet.item import Item

class Vendor:
    # Each Vendor will have an attribute named 'inventory' which is an empty list by default
    # When Vender is instantiated, optionally pass in a list with the keyword argument 'inventory'

    def __init__(self, inventory = None):

        if inventory is None:
            inventory = []

        self.inventory = inventory

    # Each instance of Vendor has an instance method named 'add' which takes in one item 
    # and adds the item to 'inventory' and returns the item that was added

    def add(self, item_to_add):
        """
        Input: one item to add to inventory
        Output: the item that is being passed in
        """
        self.inventory.append(item_to_add)

        return item_to_add

    # Each instance of Vendor has an instance method named 'remove' which takes in one item
    # and removes the matching item from the 'inventory' list 
    # and returns the item that was removed.
    # If there's no matching item in 'inventory', the method should return False
    def remove(self, item_to_remove):
        """
        Input: one item to remove from the inventory
        Output: the item that is being passed in
        """

        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False

    # Instances of Vendor have an instance method named 'get_by_category'

    def get_by_category(self, category=""):
        """
        Input: empty string as default or some string
        Output: list of items ['Computer', 'Calculator']
        """
        found_items = []

        for ele in self.inventory:
            # Loop through the inventory list in Vendor
            if category == ele.category:
                # If the category input string matches the inventory list element's category, add to list of 'found items'
                found_items.append(ele)

        return found_items

    # Instances of Vendor have an instance method named 'swap_items'
    # 'swap_items' takes in 3 arguments: 
    # One: an instance of another Vendor --> friend the vendor is swapping with
    # Two: an instance of an Item (my_item) --> item this Vendor instance plans to give
    # Three: an instance of an Item (their_item) --> item the friend Vendor plans to give

    def swap_items(self, friend_vendor, my_item, their_item):
        """
        Input: 
        1. friend_vendor is another instance of Vendor to swap Items with
        2. my_item is the item from this Vendor's inventory
        3. their_item is the item from friend's inventory

        Output: Return True if swap is successful. Otherwise, return False
        """
        

        if (my_item in self.inventory) and (their_item in friend_vendor.inventory):
            # Remove item from this Vendor's inventory
            self.inventory.remove(my_item)
            # Add to friend's inventory
            friend_vendor.inventory.append(my_item)

            # Remove item from friend's inventory
            friend_vendor.inventory.remove(their_item)
            # Add item to this Vendor's inventory
            self.inventory.append(their_item)

            return True
        else:
            return False
