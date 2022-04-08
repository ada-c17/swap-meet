
import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.vendor import Vendor

#@pytest.mark.skip
def test_items_have_age_as_float():
    items = [
        Clothing(age=3.5),
        Decor(age=3.5),
        Electronics(age=3.5)
    ]
    for item in items:
        assert item.age == pytest.approx(3.5)

#@pytest.mark.skip
def test_newest_by_category():
    item_a = Clothing(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Clothing(age=4.0)
    item_d = Decor(age=5.0)
    item_e = Clothing(age=3.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    newest_item = tai.get_newest_by_category("Clothing")

    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

#@pytest.mark.skip
def test_newest_by_category_no_matches_is_none():
    item_a = Decor(age=2.0)
    item_b = Decor(age=2.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    newest_item = tai.get_newest_by_category("Electronics")

    assert newest_item is None

#@pytest.mark.skip
def test_newest_by_category_with_duplicates():
    # Arrange
    item_a = Clothing(age=2.0)
    item_b = Clothing(age=4.0)
    item_c = Clothing(age=2.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # Act
    newest_item = tai.get_newest_by_category("Clothing")

    # Assert
    assert newest_item.category == "Clothing"
    assert newest_item.age == pytest.approx(2.0)

#@pytest.mark.skip
def test_swap_newest_by_category():
    # Arrange
    # me
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
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
    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That the results is truthy
    assert result == True
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, including the items which were swapped from one vendor to the other
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_a not in tai.inventory

#@pytest.mark.skip
def test_swap_newest_by_category_reordered():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Decor"
    )

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is truthy
    assert result == True
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in tai and jesse's inventories, and that the items that were swapped are not there
    assert item_d in tai.inventory
    assert item_a in jesse.inventory
    assert item_d not in jesse.inventory
    assert item_a not in tai.inventory  

#@pytest.mark.skip
def test_swap_newest_by_category_no_inventory_is_false():
    tai = Vendor(
        inventory=[]
    )

    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    jesse = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    result = tai.swap_newest_by_category(
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
def test_swap_best_by_category_no_other_inventory_is_false():
    item_a = Clothing(condition=2.0)
    item_b = Decor(condition=4.0)
    item_c = Clothing(condition=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    jesse = Vendor(
        inventory=[]
    )

    result = tai.swap_newest_by_category(
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
def test_swap_newest_by_category_no_match_is_false():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Clothing",
        their_priority="Clothing"
    )

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    assert result == False
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3    
    # - That all the correct items are in tai and jesse's inventories
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

#@pytest.mark.skip
def test_swap_newest_by_category_no_other_match_is_false():
    # Arrange
    item_a = Decor(age=2.0)
    item_b = Electronics(age=4.0)
    item_c = Decor(age=4.0)
    tai = Vendor(
        inventory=[item_c, item_b, item_a]
    )

    item_d = Clothing(age=2.0)
    item_e = Decor(age=4.0)
    item_f = Clothing(age=4.0)
    jesse = Vendor(
        inventory=[item_f, item_e, item_d]
    )

    # Act
    result = tai.swap_newest_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    #raise Exception("Complete this test according to comments below.")
    # *********************************************************************
    # ****** Complete Assert Portion of this test **********
    # *********************************************************************
    # Assertions should check:
    # - That result is falsy
    result == False
    # - That tai and jesse's inventories are the correct length
    assert len(tai.inventory) == 3
    assert len(jesse.inventory) == 3    
    # - That all the correct items are in tai and jesse's inventories
    assert item_a in tai.inventory
    assert item_b in tai.inventory
    assert item_c in tai.inventory
    assert item_d in jesse.inventory
    assert item_e in jesse.inventory
    assert item_f in jesse.inventory

