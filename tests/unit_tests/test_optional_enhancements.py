import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_swap_newest():
    #Act
    item_a = Item(age=1)
    item_b = Item(age=0.5)
    item_c = Item(age=3)
    sasha = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=2)
    item_e = Item(age=4)
    dasha = Vendor(
        inventory=[item_d, item_e]
    )
    #Arrange
    result = sasha.swap_by_newest(dasha)
    #Assert
    assert result == True
    assert len(sasha.inventory) == 3
    assert len(dasha.inventory) == 2
    assert sasha.inventory == [item_a, item_c, item_d]
    assert dasha.inventory == [item_e, item_b]

def test_swap_newest_with_duplicates():
    #Act
    item_a = Item(age=2)
    item_b = Item(age=1)
    item_c = Item(age=1)
    sasha = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Item(age=4)
    item_e = Item(age=3)
    item_f = Item(age=2)

    dasha = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    #Arrange
    result = sasha.swap_by_newest(dasha)
    #Assert
    assert result == True
    assert len(sasha.inventory) == 3
    assert len(dasha.inventory) == 3
    assert sasha.inventory == [item_a, item_c, item_f]
    assert dasha.inventory == [item_d, item_e, item_b]
    
def test_swap_newest_no_inventory_returns_false():
    #Act
    sasha = Vendor(
        inventory=[]
    )

    item_d = Item(age=4)
    item_e = Item(age=3)
    item_f = Item(age=2)

    dasha = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    #Arrange
    result = sasha.swap_by_newest(dasha)
    #Assert
    assert result == False
    assert len(sasha.inventory) == 0
    assert len(dasha.inventory) == 3
    assert sasha.inventory == []
    assert dasha.inventory == [item_d, item_e, item_f]
    
def test_swap_newest_no_other_inventory_returns_false():
    #Act
    item_a = Item(age=2)
    item_b = Item(age=1)
    item_c = Item(age=1)

    sasha = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    dasha = Vendor(
        inventory=[]
    )
    #Arrange
    result = sasha.swap_by_newest(dasha)
    #Assert
    assert result == False
    assert len(sasha.inventory) == 3
    assert len(dasha.inventory) == 0
    assert sasha.inventory == [item_a, item_b, item_c]
    assert dasha.inventory == []