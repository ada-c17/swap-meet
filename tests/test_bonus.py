import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_get_newest_item():
    item_a = Clothing(age=2)
    item_b = Decor(age=1)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest_item( )

    assert newest_item == item_b
    
#@pytest.mark.skip
def test_swap_newest():
    # Arrange
    # me
    item_a = Decor(age=5)
    item_b = Electronics(age=4)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=4)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    # Act
    result = tai.swap_by_newest(other=jesse)

    #assert result==True
    assert len(jesse.inventory)==3
    assert len(tai.inventory)==3
    assert item_f in tai.inventory
    assert item_c in jesse.inventory


#@pytest.mark.skip
def test_swap_newest_duplicate_age():
    # Arrange
    # me
    item_a = Decor(age=5)
    item_b = Electronics(age=2)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=1)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    # Act
    result = tai.swap_by_newest(other=jesse)

    #assert result==True
    assert len(jesse.inventory)==3
    assert len(tai.inventory)==3
    assert item_e in tai.inventory
    assert item_b in jesse.inventory
    

#@pytest.mark.skip
def test_swap_newest_all_the_same_age():
    # Arrange
    # me
    item_a = Decor(age=2)
    item_b = Electronics(age=2)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=1)
    item_e = Decor(age=1)
    item_f = Clothing(age=1)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )
    # Act
    result = tai.swap_by_newest(other=jesse)

    #assert result==True
    assert len(jesse.inventory)==3
    assert len(tai.inventory)==3
    assert item_d in tai.inventory
    assert item_a in jesse.inventory


#@pytest.mark.skip
def test_age_zero():
    # Arrange
    # me
    item_a = Decor(age=0)
    item_b = Electronics(age=2)
    item_c = Decor(age=2)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )
    # Act
    result = tai.get_newest_item()

    #assert result==True
    assert len(tai.inventory)==3
    assert result==False
        
    
