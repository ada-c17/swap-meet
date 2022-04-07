import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_get_newest():
    # Arrange 
    item_a = Decor(condition=2.0, age=0)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=67)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    # Act 
    result = tai.get_newest()

    # Assert 
    assert result == item_a
    assert len(tai.inventory) == 3 

def test_get_newest_duplicate():
    # Arrange 
    item_a = Decor(condition=2.0, age=1)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=1)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    # Act 
    result = tai.get_newest()

    # Assert 
    assert result == item_a
    assert len(tai.inventory) == 3 

def test_get_newest_no_inventory():
    # Arrange 
    tai = Vendor(
        inventory=[]
    )
    # Act 
    result = tai.get_newest()

    # Assert 
    assert result == None
    assert len(tai.inventory) == 0 


def test_swap_by_newest():
    # Arrange
    item_a = Decor(condition=2.0, age=0)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=67)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(condition=2.0, age=2)
    item_e = Decor(condition=4.0, age=15)
    item_f = Clothing(condition=4.0, age=100)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )
    # Assert 
    assert result == True
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3 
    assert item_a in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory
    assert item_d in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(condition=4.0, age=67)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=2.0, age=0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Decor(condition=4.0, age=15)
    item_e = Clothing(condition=2.0, age=2)
    item_f = Clothing(condition=4.0, age=100)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )
    # Assert 
    assert result == True
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 3 
    assert item_d in jesse.inventory
    assert item_c in jesse.inventory
    assert item_f in jesse.inventory
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_e in tai.inventory
    

    
def test_swap_by_newest_no_self_inventory_is_false():
    # Arrange
    tai = Vendor(
        inventory=[]
    )

    item_d = Decor(condition=4.0, age=15)
    item_e = Clothing(condition=2.0, age=2)
    item_f = Clothing(condition=4.0, age=100)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )
    # Assert 
    assert result == False
    assert len(jesse.inventory) == 3
    assert len(tai.inventory) == 0
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

def test_swap_by_newest_no_other_inventory_is_false():
    # Arrange
    item_a = Decor(condition=2.0, age=0)
    item_b = Electronics(condition=4.0, age=3)
    item_c = Decor(condition=4.0, age=67)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
    )
    # Assert 
    assert result == False
    assert len(jesse.inventory) == 0
    assert len(tai.inventory) == 3 
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory