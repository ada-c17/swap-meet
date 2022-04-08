import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_item_has_age():
    #arrange
    age = 1
    category = "clothing"
    condition = 4

    #act:
    item_x = Item(age, category=category,condition=condition)

    #assert
    assert item_x.age == 1

#@pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    
    assert result is True
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3 
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert item_a in jesse.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory 
    assert item_d in tai.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


#@pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )


    assert result is True
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3  
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there
    assert item_a in jesse.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory 
    assert item_d in tai.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


#@pytest.mark.skip
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

    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    assert not result
    assert len(tai.inventory) == 0
    assert len(jesse.inventory) == 3
    assert item_a in jesse.inventory
    assert item_b in jesse.inventory
    assert item_c in jesse.inventory

#@pytest.mark.skip
def test_swap_by_newest_no_other_inventory_is_false():
    item_a = Clothing(age=2)
    item_b = Decor(age=4)
    item_c = Clothing(age=4)
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

#@pytest.mark.skip
def test_swap_by_newest_no_match_is_false():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )


    assert result is False
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3  
    # - That all the correct items are in tai and jesse's inventories
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory


#@pytest.mark.skip
def test_swap_by_newest_no_other_match_is_false():
    # Arrange
    item_a = Decor(age=2)
    item_b = Electronics(age=4)
    item_c = Decor(age=4)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=4)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )



    assert result is False
    assert len(tai.inventory) == 3 and len(jesse.inventory) == 3  
    # - That all the correct items are in tai and jesse's inventories
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory    