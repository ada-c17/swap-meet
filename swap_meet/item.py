class Item:

    def __init__(self, category="", condition=0):
        # Each 'Item' will have an attribute named 'category' that is an empty string by default
        self.category = category
        self.condition = condition

    # String-ify 'Item' using 'str()'
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        # range 0 - 1.5 --> "Don't touch with bare hands"
        # range 1.5 - 2.5 --> "Is it worth it? Probably not."
        # range 2.5 - 3.5 --> "Meh, it's neutral."
        # range 3.5 - 4.5 --> "It's a goooood find."
        # range 4.5 - 5 --> "Top tier item! Must have."
        
        pass
