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
      self_first_item = self.inventory[0]
      vendor_first_item = vendor.inventory[0]
      swapped_item = self.swap_items(vendor, self_first_item, vendor_first_item)
      return True
    else:
      return False

  def get_best_by_category(self, string_category):
    max_condition = 0
    stored_item = None 
    inventory_by_cat = self.get_by_category(string_category)
    for item in inventory_by_cat:
      if item.condition >= max_condition:
        max_condition = item.condition
        stored_item = item #include this to return item
    return stored_item

  def swap_best_by_category(self,other,my_priority,their_priority):
    best_self_item = self.get_best_by_category(their_priority)
    best_their_item = other.get_best_by_category(my_priority)
    best_item_swapped = self.swap_items(other, best_self_item, best_their_item)
    return best_item_swapped #should be True

  # def swap_by_newest(self, age):
  #   stored_age = self.get_best_by_category(age)
  #   print(stored_age.age)
  #   return stored_age