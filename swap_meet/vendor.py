class Vendor:
    # Each Vendor will have an attribute named 'inventory' which is an empty list by default
    # When Vender is instantiated, optionally pass in a list with the keyword argument 'inventory'

    def __init__(self, inventory = []):

        self.inventory = inventory

    # Each instance of Vendor has an instance method named 'add' which takes in one item 
    # and adds the item to 'inventory' and returns the item that was added

    def add(self, item_to_add):
        self.inventory.append(item_to_add)

        return item_to_add

    # Each instance of Vendor has an instance method named 'remove' which takes in one item
    # and removes the matching item from the 'inventory' list 
    # and returns the item that was removed.
    # If there's no matching item in 'inventory', the method should return False
    def remove(self, item_to_remove):
        
        if item_to_remove in self.inventory:
            # print(self.inventory.remove(item_to_remove))
            # print(item_to_remove)
            # print("MATCH")
            self.inventory.remove(item_to_remove)
            # print("WORKED")
            return item_to_remove
        else:
            return False
