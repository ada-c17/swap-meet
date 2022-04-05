class Item:
    
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
# Items have age
# Add an age attribute to all Items
# Implement a Vendor method named swap_by_newest, using any logic that seems appropriate
# Write unit tests for swap_by_newest

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        # how should this handle floats?
        condition_dict = {
            1: "Don't buy it",
            2: "At your own risk",
            3: "Meh",
            4: "Near perfect",
            5: "Never been used"
        }
        return condition_dict[self.condition]