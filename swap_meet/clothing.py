from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition = 0.0):
        super().__init__('Clothing', condition)
    
    def __str__(self):
        return "The finest clothing you could wear."
#_____________________
# class Clothing:
#     def __init__(self, condition = 0.0):
#         self.category = 'Clothing'
#         self.condition = condition
        
#     from swap_meet.item import Item
#     def __str__(self):
#         return "The finest clothing you could wear."

#     def condition_description(self):
#         if self.condition >=0 and self.condition <1:
#             return 'heavily_used'
#         elif self.condition >=1 and self.condition <2:
#             return 'often_used'
#         elif self.condition >=2 and self.condition <3:
#             return 'moderately_used'
#         elif self.condition >=3 and self.condition <4:
#             return 'occasionally_used'
#         elif self.condition >=4 and self.condition <5:
#             return 'rarely_used'
#         else:
#             return 'mint'




