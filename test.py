class Item:
    def __init__(self, category = "", condition=0.0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        return f"The quality of this item is {self.condition}."

class Clothing(Item):
    def __init__(self, condition):
        super().__init__(condition=condition)
        self.category = "Clothing"

    def __str__(self):
        return "The finest clothing you could wear."








def display_item(item):
    print(item.category)
    print(item)
    print(item.condition_description())

shirt = Clothing(3.5)
display_item(shirt)
