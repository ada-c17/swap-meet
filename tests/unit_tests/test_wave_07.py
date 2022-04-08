import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(condition=2.0,age=5)
    item_b = Electronics(condition=4.0,age=2)
    item_c = Decor(condition=4.0,age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0,age=7)
    item_e = Decor(condition=4.0,age=6)
    item_f = Clothing(condition=4.0,age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse
    )

    # Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_f in tai.inventory
    assert item_b in jesse.inventory
    assert item_b not in tai.inventory
    assert item_f not in jesse.inventory

# @pytest.mark.skip
def test_swap_by_newest_best():
    # Arrange
    # me
    item_a = Decor(condition=2.0,age=2)
    item_b = Electronics(condition=4.0,age=2)
    item_c = Decor(condition=4.0,age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(condition=2.0,age=1)
    item_e = Decor(condition=4.0,age=6)
    item_f = Clothing(condition=4.0,age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        best=True
    )

    # Assert
    assert result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    assert item_f in tai.inventory
    assert item_b in jesse.inventory
    assert item_b not in tai.inventory
    assert item_f not in jesse.inventory


# @pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0,age=7)
    item_b = Decor(condition=4.0,age=6)
    item_c = Clothing(condition=4.0,age=1)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

# @pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
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
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory