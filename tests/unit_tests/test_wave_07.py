import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics


def test_get_newest():
    item_a = Clothing(age=5)
    item_b = Electronics(age=2)
    item_c = Clothing(age=5)
    item_d = Decor(age=1)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest()

    assert newest_item.category == "Decor"
    assert newest_item.age == pytest.approx(1.0)


def test_newest_when_inventory_is_empty():
    
    tai = Vendor(inventory=[])

    newest_item = tai.get_newest()

    assert newest_item is None


def test_newest_with_duplicates():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Clothing(age=4)
    item_c = Clothing(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    newest_item = tai.get_newest()

    # Assert
    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

def test_swap_newest():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=3)
    item_c = Decor(age=5)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=21)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(other=jesse)

    
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    assert result == True
    # - That tai and jesse's inventories are the correct length
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert item_a not in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_f in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f not in jesse.inventory
    assert item_a in jesse.inventory



def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_by_newest(other=jesse)

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory


def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_by_newest(other=jesse)

    assert not result
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 0
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
