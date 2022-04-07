"""

### Wave 2

In Wave 2 we will create the `Item` class and the `get_by_category` method.

- There is a module (file) named `item.py` inside of the `swap_meet` package (folder)

- Inside this module, there is a class named `Item`
- Each `Item` will have an attribute named `category`, which is an empty string by default

### Wave 3

- we will write a method to stringify an `Item` using `str()` 

- When we stringify (convert to a string) an instance of `Item` using `str()`, it returns `"Hello World!"`
  - This implies `Item` overrides its stringify method. We may need to research the `__str__` method for more details!

- All three classes and the `Item` class have an instance method named `condition_description`, 
which should describe the condition in words based on the value, assuming they all range from 0 to 5. 
These can be basic descriptions (eg. 'mint', 'heavily used') but feel free to have fun with these 
(e.g. 'You probably want a glove for this one..."). The one requirement is that the `condition_description` 
for all three classes above have the same behavior.

"""
#from swap_meet.vendor import Vendor

class Item:
    def __init__(self, category = None, condition = 0):
        if not category:
            category = ""
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if 0 <= self.condition <= 1:
            return "Is okie"
        elif self.condition <= 2:
            return "Not tooo bad"
        elif self.condition <= 3:
            return "Could be worse"
        elif self.condition <= 4:
             return "Not great"
        elif self.condition <= 5:
            return "Bad, very bad"

    pass