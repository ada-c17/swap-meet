class Item:

    def __init__(self, category=""):
        # Each 'Item' will have an attribute named 'category' that is an empty string by default
        self.category = category
    
    
    # String-ify 'Item' using 'str()'
    def __str__(self):
        return "Hello World!"


    # Write the method 'swap_items'
