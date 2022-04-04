class Vendor:
    def __init__(self,inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
    
    def add(self,*items):
        if not items:
            return None
        for item in items:
            self.inventory.append(item)
        return items[0] if len(items) == 1 else items
    
    def remove(self,*items):
        if not items:
            return None
        for item in items:
            if item not in self.inventory:
                return False
            self.inventory.remove(item)
        return items[0] if len(items) == 1 else items
