# Wave 1
class Vendor:
    """
    attributes: inventory
    methods : add and remove
    """
    
    def __init__(self, inventory = None):
        """Inventory is keyword argument that optionally pass in."""
        # assign empty list to inventory when the if statement is falsy. 
        # Otherwise, assign inventory as value of object's inventory.
        if not inventory:
            inventory = []
        self.inventory = inventory
        
        
    def add(self, item):
        """Adding new item into inventory and returns the added item."""
        self.inventory.append(item)
        return item


    def remove(self, item):
        """Removing item from inventory if it is matching the paramenter item and returns the removed item."""
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False
        