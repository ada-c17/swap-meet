# Wave 2

#from swap_meet.vendor import Vendor
class Item:
    """
    attributes: category
    methods: get_by_category
    """

    def __init__(self, category = None):
        """category is keyword argument that optionally pass in."""
        # assign empty string to category when the if statement is falsy. 
        # Otherwise, assign category as value of object's category.
        if category is None:
            category = ""
        self.category = category


    def __str__(self):
        """Return string with 'Hellow World!' """
        return str("Hello World!")

