import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item

# @pytest.mark.skip
def test_get_newest_by_category():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    sam = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    # Act
    newest_item = sam.get_newest_by_category("Decor")

    # Assert
    assert len(sam.inventory)== 5
    assert newest_item == item_b
    assert newest_item.category == "Decor"
    assert newest_item.age == 2


# @pytest.mark.skip
def test_get_newest_by_category_no_match_is_none():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=5)
    item_e = Clothing(age=3)
    sam = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    # Act
    newest_item = sam.get_newest_by_category("Electronics")

    # Assert
    assert len(sam.inventory)== 5
    assert newest_item is None


# @pytest.mark.skip
def test_get_newest_by_category_with_empty_inventory():
    # Arrange
    sam = Vendor(
        inventory=[]
    )

    # Act
    newest_item = sam.get_newest_by_category("Decor")

    # Assert
    assert len(sam.inventory)== 0
    assert newest_item is None


# @pytest.mark.skip
def test_get_newest_by_category_no_duplicate():
    # Arrange
    item_a = Clothing(age=2)
    item_b = Decor(age=2)
    item_c = Clothing(age=4)
    item_d = Decor(age=2)
    item_e = Clothing(age=3)
    sam = Vendor(
        inventory=[item_a, item_b, item_c, item_d, item_e]
    )

    # Act
    newest_item = sam.get_newest_by_category("Decor")

    # Assert
    assert len(sam.inventory)== 5
    assert newest_item.category == "Decor"
    assert newest_item.age == 2


# @pytest.mark.skip
def test_swap_newest_by_category():
    # Arrange
    # me
    item_a = Electronics(age=2)
    item_b = Decor(age=2)
    item_c = Electronics(age=4)
    sunny = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=1)
    item_f = Decor(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = sunny.swap_newest_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Electronics"
    )

    # Assert
    # - That the results is truthy
    assert result is True
    # - That sunny and jesse's inventories are the correct length
    assert len(sunny.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in sunny and jesse's inventories, including the items which were swapped from one vendor to the other
    # test items are in sunny's inventories
    assert sunny.inventory[0] == item_b
    assert sunny.inventory[0].category == "Decor"
    assert sunny.inventory[0].age == 2
    assert sunny.inventory[1] == item_c
    assert sunny.inventory[1].category == "Electronics"
    assert sunny.inventory[1].age == 4
    assert sunny.inventory[2] == item_e
    assert sunny.inventory[2].category == "Decor"
    assert sunny.inventory[2].age == 1
    # test swapped item is not in the sunny's inventory
    for item in sunny.inventory:
        assert item != item_a
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].age == 2
    assert jesse.inventory[1] == item_f
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].age == 4
    assert jesse.inventory[2] == item_a
    assert jesse.inventory[2].category == "Electronics"
    assert jesse.inventory[2].age == 2
    # test swapped item is not in the jesse's inventory
    for item in jesse.inventory:
        assert item != item_e


# @pytest.mark.skip
def test_swap_newest_by_category_reorder():
    # Arrange
    # me
    item_a = Electronics(age=2)
    item_b = Decor(age=2)
    item_c = Electronics(age=4)
    sunny = Vendor(
        inventory=[item_b, item_a, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=1)
    item_f = Decor(age=4)
    jesse = Vendor(
        inventory=[item_e, item_f, item_d]
    )

    # Act
    result = sunny.swap_newest_by_category(
        other=jesse,
        my_priority="Decor",
        their_priority="Electronics"
    )

    # Assert
    # - That the results is truthy
    assert result is True
    # - That sunny and jesse's inventories are the correct length
    assert len(sunny.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in sunny and jesse's inventories, including the items which were swapped from one vendor to the other
    # test items are in sunny's inventories
    assert sunny.inventory[0] == item_b
    assert sunny.inventory[0].category == "Decor"
    assert sunny.inventory[0].age == 2
    assert sunny.inventory[1] == item_c
    assert sunny.inventory[1].category == "Electronics"
    assert sunny.inventory[1].age == 4
    assert sunny.inventory[2] == item_e
    assert sunny.inventory[2].category == "Decor"
    assert sunny.inventory[2].age == 1
    # test swapped item is not in the sunny's inventory
    for item in sunny.inventory:
        assert item != item_a
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_f
    assert jesse.inventory[0].category == "Decor"
    assert jesse.inventory[0].age == 4
    assert jesse.inventory[1] == item_d
    assert jesse.inventory[1].category == "Clothing"
    assert jesse.inventory[1].age == 2
    assert jesse.inventory[2] == item_a
    assert jesse.inventory[2].category == "Electronics"
    assert jesse.inventory[2].age == 2
    # test swapped item is not in the jesse's inventory
    for item in jesse.inventory:
        assert item != item_e


# @pytest.mark.skip
def test_swap_newest_by_category_no_other_match_is_false():
    # Arrange
    # me
    item_a = Electronics(age=2)
    item_b = Decor(age=2)
    item_c = Electronics(age=4)
    sunny = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=1)
    item_f = Decor(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = sunny.swap_newest_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # Assert
    # - That the results is truthy
    assert result is False
    # - That tai and jesse's inventories are the correct length
    assert len(sunny.inventory) == 3
    assert len(jesse.inventory) == 3
    # - That all the correct items are in sunny and jesse's inventories
    # test items are in sunny's inventories
    assert sunny.inventory[0] == item_a
    assert sunny.inventory[0].category == "Electronics"
    assert sunny.inventory[0].age == 2
    assert sunny.inventory[1] == item_b
    assert sunny.inventory[1].category == "Decor"
    assert sunny.inventory[1].age == 2
    assert sunny.inventory[2] == item_c
    assert sunny.inventory[2].category == "Electronics"
    assert sunny.inventory[2].age == 4
    
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].age == 2
    assert jesse.inventory[1] == item_e
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].age == 1
    assert jesse.inventory[2] == item_f
    assert jesse.inventory[2].category == "Decor"
    assert jesse.inventory[2].age == 4


# @pytest.mark.skip
def test_swap_newest_by_category_with_my_empty_inventory():
    # Arrange
    # me
    sunny = Vendor(
        inventory=[]
    )

    # them
    item_d = Clothing(age=2)
    item_e = Decor(age=1)
    item_f = Decor(age=4)
    jesse = Vendor(
        inventory=[item_d, item_e, item_f]
    )

    # Act
    result = sunny.swap_newest_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # Assert
    # - That the results is truthy
    assert result is False
    # - That sunny and jesse's inventories are the correct length
    assert len(sunny.inventory) == 0
    assert len(jesse.inventory) == 3
    # test items are in jesse's inventories
    assert jesse.inventory[0] == item_d
    assert jesse.inventory[0].category == "Clothing"
    assert jesse.inventory[0].age == 2
    assert jesse.inventory[1] == item_e
    assert jesse.inventory[1].category == "Decor"
    assert jesse.inventory[1].age == 1
    assert jesse.inventory[2] == item_f
    assert jesse.inventory[2].category == "Decor"
    assert jesse.inventory[2].age == 4
    

# @pytest.mark.skip
def test_swap_newest_by_category_with_other_empty_inventory():
    # Arrange
    # me
    item_a = Electronics(age=2)
    item_b = Decor(age=2)
    item_c = Electronics(age=4)
    sunny = Vendor(
        inventory=[item_a, item_b, item_c]
    )

    # them
    jesse = Vendor(
        inventory=[]
    )

    # Act
    result = sunny.swap_newest_by_category(
        other=jesse,
        my_priority="Electronics",
        their_priority="Decor"
    )

    # Assert
    # - That the results is truthy
    assert result is False
    # - That sunny and jesse's inventories are the correct length
    assert len(sunny.inventory) == 3
    assert len(jesse.inventory) == 0
    # - That all the correct items are in sunny's inventories
    # test items are in sunny's inventories
    assert sunny.inventory[0] == item_a
    assert sunny.inventory[0].category == "Electronics"
    assert sunny.inventory[0].age == 2
    assert sunny.inventory[1] == item_b
    assert sunny.inventory[1].category == "Decor"
    assert sunny.inventory[1].age == 2
    assert sunny.inventory[2] == item_c
    assert sunny.inventory[2].category == "Electronics"
    assert sunny.inventory[2].age == 4


    