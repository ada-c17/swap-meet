import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_newest():
    item_a = Clothing(age=1.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_newest_item()

    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(1.0)



def test_newest_with_duplicates():
    # Arrange
    item_a = Clothing(age=2.0)
    item_b = Clothing(age=4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_newest_item()

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.age == pytest.approx(2.0)


def test_swap_newest():
    # Arrange
    # me
    item_a = Decor(age=1.0)
    item_b = Electronics(age=9.0)
    item_c = Decor(age=15.0)
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
    result = tai.swap_newest_item(
        other=jesse
    )

    assert result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_d in tai.inventory
    assert item_d not in jesse.inventory
    assert item_a in jesse.inventory
    assert item_a not in tai.inventory

    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other


def test_newest_reordered():
    # Arrange
    item_a = Decor(age=16.0)
    item_b = Electronics(age=70.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=5.0)
    item_e = Decor(age=3.0)
    item_f = Clothing(age=9.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_newest_item(
        other=jesse
    )

    assert result
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    assert item_e in tai.inventory
    assert item_e not in jesse.inventory
    assert item_c in jesse.inventory
    assert item_c not in tai.inventory

    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there


def test_swap_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2.0)
    item_b = Decor(age=4.0)
    item_c = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_item(
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(age=2.0)
    item_b = Decor(age = 4.0)
    item_c = Clothing(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_newest_item(
        other=jesse
    )

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory

