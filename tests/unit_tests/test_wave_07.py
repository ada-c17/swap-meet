import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#Optional Enhancements
def test_swap_newest_item():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(jesse)


    assert result == True
    assert len(tai.inventory) is 3
    assert len(jesse.inventory) is 3
    assert item_a not in tai.inventory
    assert item_a in jesse.inventory
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory