class Item:
    """
    attributes: category and conditon
    methods: __str__() and condition_description()
    """

    # Wave 2, create category attribute
    # Wave 5, create condition attribute
    def __init__(self, category = None, condition = None):
        """category and condition are keyword arguments that optionally pass in."""
        if category is None:
            category = ""
        if condition is None:
            condition = 0
        self.category = category
        self.condition = condition


    # Wave 3
    def __str__(self):
        """Return value in string format """
        return str("Hello World!")


    # Wave 5
    def condition_description(self):
        """Return item description base on its condition."""
        
        if self.condition == 0:
            return str("New condition")

        elif self.condition < 4:
            return str("Still useable")

        return str("Old or heavily used")