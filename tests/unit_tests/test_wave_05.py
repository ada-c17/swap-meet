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

    items[0].condition = 2
    two_condition_description = items[0].condition_description()
    assert isinstance(two_condition_description, str)

    for item in items:
        item.condition = 2
        assert item.condition_description() == two_condition_description

    assert two_condition_description != one_condition_description
    assert two_condition_description != five_condition_description

    items[0].condition = 3
    three_condition_description = items[0].condition_description()
    assert isinstance(three_condition_description, str)

    for item in items:
        item.condition = 3
        assert item.condition_description() == three_condition_description

    assert three_condition_description != two_condition_description
    assert three_condition_description != one_condition_description
    assert three_condition_description != five_condition_description

    items[0].condition = 4
    four_condition_description = items[0].condition_description()
    assert isinstance(four_condition_description, str)

    for item in items:
        item.condition = 4
        assert item.condition_description() == four_condition_description

    assert four_condition_description != three_condition_description
    assert four_condition_description != two_condition_description
    assert four_condition_description != one_condition_description
    assert four_condition_description != five_condition_description

    items[0].condition = 0
    zero_condition_description = items[0].condition_description()
    assert isinstance(zero_condition_description, str)

    for item in items:
        item.condition = 0
        assert item.condition_description() == zero_condition_description

    assert zero_condition_description != four_condition_description
    assert zero_condition_description != three_condition_description
    assert zero_condition_description != two_condition_description
    assert zero_condition_description != one_condition_description
    assert zero_condition_description != five_condition_description


