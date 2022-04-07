class Item:

    def __init__(self, category="", condition=0):
        # Each 'Item' will have an attribute named 'category' that is an empty string by default
        self.category = category
        self.condition = condition

    def __str__(self):
        """
        String-ify an instance of 'Item' using 'str()'
        """
        return "Hello World!"
    
    def condition_description(self):

        """
        This function provides an item description based on self.condition
        
        * Condition 0 - 1 --> "Don't touch with bare hands"
        * Condition 1 - 2 --> "Is it worth it? Probably not."
        * Condition 2 - 3 --> "Meh, it's neutral."
        * Condition 3 - 4 --> "It's a good find."
        * Condition 4 - 5 --> "Top tier item! Must have."
        """

        if (self.condition >= 0) and (self.condition <= 1):
            return "Don't touch with bare hands."
        elif (self.condition > 1) and (self.condition <= 2):
            return "Is it worth it? Probably not."
        elif (self.condition > 2) and (self.condition <= 3):
            return "Meh, it's neutral."
        elif (self.condition > 3) and (self.condition <= 4):
            return "It's a good find."
        elif (self.condition > 4) and (self.condition <= 5):
            return "Top tier item! Must have."