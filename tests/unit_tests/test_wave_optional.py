import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_swap_by_newest_between_good_vendors():
    # Arrange
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_c, item_b, item_a],
        trait="Good"
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=2)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d],
        trait="Good"
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_b, item_a, item_f]
    assert jesse.inventory == [item_e, item_d, item_c]


def test_swap_by_newest_between_evil_vendors():
    # Arrange
    item_a = Decor(condition=2.0, age=3)
    item_b = Electronics(condition=4.0)
    item_c = Decor(condition=4.0, age=3)
    tai = Vendor(
        inventory=[item_c, item_b, item_a],
        trait = "Evil"
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0)
    item_f = Clothing(condition=4.0, age=2)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d],
        trait="Evil"
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert tai.inventory == [item_c, item_b, item_d]
    assert jesse.inventory == [item_f, item_e, item_a]


def test_swap_by_newest_no_match_is_False():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Decor",
        their_priority="Clothing"
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory