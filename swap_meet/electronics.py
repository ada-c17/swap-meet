from swap_meet.item import Item
#wave 5: - `Electronics`/child class of Item class. category attribute is Electronics. the strigfy method returns A gadget full of buttons and secrets."
class Electronics(Item):
     def __init__(self,category="Electronics", condition= 0 ):
      super().__init__(category , condition)
     def __str__(self):
      return "A gadget full of buttons and secrets."
   



