from item import Item

class Vendor():
    # create inventory parameters, where deafalt is empty list
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory
    

    # create instance method add which add things in inventory list
    def add(self,item):
        self.inventory.append(item)
        return item


    # create instance method remove which remove item from inventory list
    def remove(self,item):
        for items in self.inventory:
            if item == items:
                self.inventory.remove(items)
                return items
        return False


    # create instance method which return a list of Items in the inventory with that category
    def get_by_category(self,category):
        list_of_items = []
        for item in self.inventory:
            if category == item.category:
                list_of_items.append(item)
        return list_of_items


    # create instance method implement swaping process
    def swap_items(self, another_vendor, my_item, their_item):
        
        if not my_item or not their_item:
            return False
        
        else:
            
            if my_item in self.inventory and their_item in another_vendor.inventory:
                # vendor swap his item
                self.remove(my_item)
                another_vendor.add(my_item)
                # friend swap his item
                another_vendor.remove(their_item)
                self.add(their_item)
                return True

item_a = Item(category="clothing")
item_b = Item(category="clothing")
item_c = Item(category="clothing")
fatimah = Vendor(
    inventory=[item_a, item_b, item_c]
)

item_d = Item(category="electronics")
item_e = Item(category="decor")
jolie = Vendor(
    inventory=[item_d, item_e]
)

print(fatimah.inventory)
print(jolie.inventory)

result = fatimah.swap_items(jolie, item_b, item_d)
print(fatimah.inventory)
print(jolie.inventory)