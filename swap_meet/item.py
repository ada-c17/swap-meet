class Item:
    """Parent class of Clothing, Decor, and Electronics"""

    # Wave 2, create category attribute
    # Wave 5, create condition attribute
    def __init__(self, category = None, condition = None, age = None):
        """category and condition are keyword arguments that optionally pass in."""
        if not category:
            category = ""
        if not condition:
            condition = 0
        if not age:
            age = 0
        self.category = category
        self.condition = condition
        self.age = age
        

    # Wave 3
    def __str__(self):
        """Printing the returning message string when printing instance of Item class."""
        return "Hello World!"


    # Wave 5
    def condition_description(self):
        """Return item description base on its condition."""
        # validate the condition value before 
        if isinstance(self.condition, int) or isinstance(self.condition, float):
            if self.condition < 1:
                return "New condition"
            elif self.condition < 4:
                return "Still useable"
            return "Old or heavily used"
        return "Invalid input value!"