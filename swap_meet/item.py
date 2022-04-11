class Item:
    def __init__(self, category="", condition=0.0, age=None):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0.0:
            return "Condition unknown or not supplied."
        elif self.condition > 0.0 and self.condition <= 1.0:
            return "This should be swapped into the dumpster."
        elif self.condition > 1.0 and self.condition <= 2.0:
            return "This item's condition is as dubious as leftovers you forgot about."
        elif self.condition > 2.0 and self.condition <= 3.0:
            return "This item is okay, nothing to get excited about."
        elif self.condition > 3.0 and self.condition <= 4.0:
            return "This item is in above average condition! Score!"
        elif self.condition > 4.0:
            return "This item's condition is suspiciously good. You definitely want it!"