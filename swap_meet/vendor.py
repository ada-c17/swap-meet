class Vendor():
  def __init__ (self, inventory = None):
    if inventory is None: #do not want mutable object
      inventory = [] #as a parameter, so I set to None
    self.inventory = inventory #empty list
  
  def add(self, item):
    self.inventory.append(item)
    return item

  def remove(self, item):
    if item in self.inventory:
      self.inventory.remove(item)
      return item
    else:
      return False
  def get_by_category(self,string_category):
    inventory_same_category = []
    for item in self.inventory:
      if item.category == string_category: #we want category here
        inventory_same_category.append(item) #only append item associated with category
    return inventory_same_category#list of inventory
  
  def swap_items(self, vendor, my_item, their_item):
    if my_item in self.inventory and their_item in vendor.inventory:
      self.inventory.remove(my_item)
      vendor.inventory.append(my_item)
      vendor.inventory.remove(their_item)
      self.inventory.append(their_item)
      return True
    else:
      return False

  def swap_first_item(self, vendor):
    if len(vendor.inventory) and len(self.inventory) != 0:
      self_item = self.inventory[0]
      vendor_item = vendor.inventory[0]
      
      self.inventory.remove(self_item)
      vendor.inventory.append(self_item)
      vendor.inventory.remove(vendor_item)
      self.inventory.append(vendor_item)
      return True
    else:
      return False