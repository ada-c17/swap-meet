import re
import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

# @pytest.mark.skip
def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."

# @pytest.mark.skip
def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category == "Decor"
    assert str(decor) == "Something to decorate your space."

# @pytest.mark.skip
def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category == "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."

# @pytest.mark.skip
def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

# @pytest.mark.skip
def test_items_have_condition_descriptions_that_are_the_same_regardless_of_type():
    items = [
        Clothing(condition=5),
        Decor(condition=5),
        Electronics(condition=5)
    ]
    five_condition_description = items[0].condition_description()
    assert isinstance(five_condition_description, str)
    for item in items:
        assert item.condition_description() == five_condition_description

    items[0].condition = 1
    one_condition_description = items[0].condition_description()
    assert isinstance(one_condition_description, str)

    for item in items:
        item.condition = 1
        assert item.condition_description() == one_condition_description

    assert one_condition_description != five_condition_description

# Additional test cases on condition_description() function to complete the code coverage
# @pytest.mark.skip
def test_condition_description_with_all_conditions_are_0():
    # Arrange
    items = [
        Clothing(condition=0),
        Decor(condition=0),
        Electronics(condition=0)
    ]

    # Act & Assert
    assert len(items) == 3
    for i in range(len(items)):
        assert items[i].condition_description() == "New condition"
        assert items[i].condition == 0

# @pytest.mark.skip
def test_condition_description_with_invalid_input():
    # Arrange
    items = [
        Clothing(condition="Good"),
        Decor(condition="Bad"),
        Electronics(condition="Fair")
    ]

    # Act & Assert
    assert len(items) == 3
    assert items[0].condition == "Good"
    assert items[1].condition == "Bad"
    assert items[2].condition == "Fair"
    for i in range(len(items)):
        assert items[i].condition_description() == "Invalid input value!"

