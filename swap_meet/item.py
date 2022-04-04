class Item:
    def __init__(self, category=""):
        self.category = category
    #stringify item
    def __str__(self):
        return "Hello World!"

# When we initialize an instance of Item,
# we can optionally pass in a string with the keyword argument category