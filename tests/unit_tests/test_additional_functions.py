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