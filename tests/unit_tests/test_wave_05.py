import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

#@pytest.mark.skip
def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."

#@pytest.mark.skip
def test_decor_has_default_category_and_to_str():
    decor = Decor()
    assert decor.category == "Decor"
    assert str(decor) == "Something to decorate your space."

#@pytest.mark.skip
def test_electronics_has_default_category_and_to_str():
    electronics = Electronics()
    assert electronics.category == "Electronics"
    assert str(electronics) == "A gadget full of buttons and secrets."

#@pytest.mark.skip
def test_items_have_condition_as_float():
    items = [
        Clothing(condition=3.5),
        Decor(condition=3.5),
        Electronics(condition=3.5)
    ]
    for item in items:
        assert item.condition == pytest.approx(3.5)

#@pytest.mark.skip
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

# *******************ADDING TEST*******************
def test_condition_descriptions_handles_floats_incorrect_values():
    # Arrange
    clothing1 = Clothing(condition=0.3) # Less than 1
    electronics1 = Electronics(condition=7) # Greater than 5
    clothing2 = Clothing(condition=1.6) # Floats
    clothing3 = Clothing(condition=3.1)
    clothing4 = Clothing(condition=4.0)
    clothing5 = Clothing(condition=4.5)
    decor1 = Decor(condition=1.1)
    decor2 = Decor(condition=1.5)
    decor3 = Decor(condition=2.5)
    decor4 = Decor(condition=3.5)
    decor5 = Decor(condition=4.5)
    

    # Act/Assert
    assert clothing1.condition_description() == "Don't buy it"
    assert clothing2.condition_description() == "At your own risk"
    assert clothing3.condition_description() == "Meh"
    assert clothing4.condition_description() == "Near perfect"
    assert clothing5.condition_description() == "Never been used"
    assert decor1.condition_description() == "Don't buy it"
    assert decor2.condition_description() == "At your own risk"
    assert decor3.condition_description() == "Meh"
    assert decor4.condition_description() == "Near perfect"
    assert decor5.condition_description() == "Never been used"
    assert electronics1.condition_description() == "Never been used"