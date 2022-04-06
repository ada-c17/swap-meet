class Item:

    def __init__(self, category="", condition=0):
        # Each 'Item' will have an attribute named 'category' that is an empty string by default
        self.category = category
        self.condition = condition

    # String-ify 'Item' using 'str()'
    def __str__(self):
        return "Hello World!"
