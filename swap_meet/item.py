class Item:
#   wave2:made a class named item with attribute category which is an empty string by default and we can pass it in optionally with keyword category   
#wave 5:item class and the 3 child classes will have attribute condition which can be provided in optionally in initializer with the default value 0
  def __init__(self,category="",condition=0):
       self.category = category
       self.condition=condition
  #wave3:method to stringify an `Item` using `str()` and write the method `swap_items`.
  def __str__(self):
      return "Hello World!"
  #wave 5:condition_discription is an instance method that item class and 3 children share. which describes condition of the item ranging from 0-5 in words
  
  def condition_description(self):
       if self.condition<=0:
          description = "terrible"
       elif  self.condition<=1:
          description="very bad"
       elif self.condition<=2:
          description="bad"
       elif self.condition<=3:
          description="not bad"
       elif self.condition<=4:
          description="very good"
       elif self.condition<=5:
          description="perfect"
       return description