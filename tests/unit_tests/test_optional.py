import pytest
from swap_meet.vendor import Vendor
from swap_meet.item import Item

def test_item_by_age():
    
    age_1 = Item(age=5)
    age_2 = Item(age=22)
    age_3 = Item(age=30)
    vendor = Vendor([age_1, age_2, age_3]
    )
    
    age_items = vendor.get_by_newest()

    assert age_items != age_1
    assert age_items != age_2
    assert age_items != age_3


    

