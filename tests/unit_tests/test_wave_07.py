import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item
from datetime import date

today=date.today()

# #@pytest.mark.skip
def test_best_by_age():
    item_a = Clothing(age=date(2020,2,1))
    item_b = Decor(age=date(2020,2,1))
    item_c = Clothing(age=date(2018,1,1))
    item_d = Decor(age=date(2010,9,1))
    item_e = Clothing(age=date(2011,1,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_age("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == today.year-2020

# #@pytest.mark.skip
def test_age_is_greater_then_today():
    item_a = Clothing(age=date(2024,2,1))
    item_b = Decor(age=date(2020,2,1))
    item_c = Clothing(age=date(2018,1,1))
    item_d = Decor(age=date(2010,9,1))
    item_e = Clothing(age=date(2011,1,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    best_item = tai.get_best_by_age("Clothing")

    assert best_item.category == "Clothing"
    assert best_item.age == 0    

# #@pytest.mark.skip
def test_best_by_age_no_matches_is_none():
    item_a = Decor(age=date(2020,2,1))
    item_b = Decor(age=date(2020,2,1))
    item_c = Decor(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    best_item = tai.get_best_by_age("Electronics")

    assert best_item is None

# #@pytest.mark.skip
def test_best_by_age_with_duplicates():
    # Arrange
    item_a = Clothing(age=date(2020,2,1))
    item_b = Clothing(age=date(2020,2,1))
    item_c = Clothing(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    best_item = tai.get_best_by_age("Clothing")

    # Assert
    assert best_item.category == "Clothing"
    assert best_item.age == today.year-2020    

# #@pytest.mark.skip
def test_swap_by_newest():
    # Arrange
    # me
    item_a = Decor(age=date(2020,2,1))
    item_b = Electronics(age=date(2018,2,1))
    item_c = Decor(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=date(2020,2,1))
    item_e = Decor(age=date(2018,2,1))
    item_f = Clothing(age=date(2018,2,1))
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert result ==True
    assert len(tai.inventory)==3 
    assert len(jesse.inventory)==3
    assert all(x in [item_d, item_b, item_c] for x in tai.inventory)
    assert all(x in [item_a, item_e, item_f] for x in jesse.inventory)   

# #@pytest.mark.skip
def test_swap_by_newest_reordered():
    # Arrange
    item_a = Decor(age=date(2020,2,1))
    item_b = Electronics(age=date(2018,2,1))
    item_c = Decor(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=date(2020,2,1))
    item_e = Decor(age=date(2018,2,1))
    item_f = Clothing(age=date(2018,2,1))
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there
    assert result ==True
    assert len(tai.inventory)==3 
    assert len(jesse.inventory)==3
    assert all(x in [item_d, item_b, item_c] for x in tai.inventory)
    assert all(x in [item_a, item_e, item_f] for x in jesse.inventory)

#@pytest.mark.skip
def test_swap_by_newest_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(age=date(2020,2,1))
    item_b = Decor(age=date(2018,2,1))
    item_c = Clothing(age=date(2018,2,1))
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
    item_a = Clothing(age=date(2020,2,1))
    item_b = Decor(age=date(2018,2,1))
    item_c = Clothing(age=date(2018,2,1))
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
def test_swap_best_by_newest_no_match_is_false():
    # Arrange
    item_a = Decor(age=date(2020,2,1))
    item_b = Electronics(age=date(2018,2,1))
    item_c = Decor(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=date(2020,2,1))
    item_e = Decor(age=date(2018,2,1))
    item_f = Clothing(age=date(2018,2,1))
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories
    result ==False
    assert len(tai.inventory)==3 
    assert len(jesse.inventory)==3
    assert all(x in [item_a, item_b, item_c] for x in tai.inventory)
    assert all(x in [item_d, item_e, item_f] for x in jesse.inventory)

#@pytest.mark.skip
def test_swap_best_by_newest_no_other_match_is_false():
    # Arrange
    item_a = Decor(age=date(2020,2,1))
    item_b = Electronics(age=date(2018,2,1))
    item_c = Decor(age=date(2018,2,1))
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=date(2020,2,1))
    item_e = Decor(age=date(2018,2,1))
    item_f = Clothing(age=date(2018,2,1))
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_by_newest(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    # - That tai and jesse's inventories are the correct length
    # - That all the correct items are in tai and jesse's inventories
    result ==False
    assert len(tai.inventory)==3 
    assert len(jesse.inventory)==3
    assert all(x in [item_a, item_b, item_c] for x in tai.inventory)
    assert all(x in [item_d, item_e, item_f] for x in jesse.inventory) 