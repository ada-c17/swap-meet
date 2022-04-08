import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_vendor_inventory_is_read_only():
    item_a = Decor(age=0.5)
    item_b = Electronics()
    item_c = Clothing(age=0.5)

    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    with pytest.raises(AttributeError):
        tai.inventory = [item_a]


def test_ValueError_raised_if_item_condition_less_than_0():
    with pytest.raises(ValueError, match="Condition rating must be from 0 to 5."):
        item = Decor(condition=-10)

    with pytest.raises(ValueError, match="Condition rating must be from 0 to 5."):
        item_a = Clothing(condition=-2)


def test_ValueError_raised_if_item_condition_larger_than_5():
    with pytest.raises(ValueError, match="Condition rating must be from 0 to 5."):
        item = Electronics(condition=10)
    
    with pytest.raises(ValueError, match="Condition rating must be from 0 to 5."):
        item = Item(condition=10)


def test_ValueError_raised_if_item_age_not_larger_than_0():
    with pytest.raises(ValueError, match="Age must be larger than 0."):
        item = Decor(age=0)
        
    with pytest.raises(ValueError, match="Age must be larger than 0."):
        item_a = Electronics(age=-2)
