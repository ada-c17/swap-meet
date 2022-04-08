class Item():
  def __init__ (self, category = "", age =0):
    self.category = category
    self.age = age

  def __str__(self):
    return "Hello World!"

  def condition_description(self):
    if 0 <= self.condition <= 3:
      return "Wear your gloves folks"
    elif 3 < self.condition < 4.5:
      return "Good condition"
    elif self.condition >= 4.5:
      return "Perfect condition"
