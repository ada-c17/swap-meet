import pytest
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics
from swap_meet.item import Item


# @pytest.mark.skip
def test_clothing_has_default_category_and_to_str():
    cloth = Clothing()
    assert cloth.category == "Clothing"
    assert str(cloth) == "The finest clothing you could wear."
#added
def test_Item_has_default_category_and_to_str():
    item = Item()
    assert item.category == ""
    assert str(item) == "Hello World!"

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


#added
def test_item_description_accurate():
    item2=Item(condition=2)
    item3=Item(condition=3)
    item4=Item(condition=4)
    item5=Item(condition=5)
    item1=Item(condition=0.5)
    assert item1.condition_description()=="very bad"
    assert item2.condition_description()=="bad"
    assert item3.condition_description()=="not bad"
    assert item4.condition_description()=="very good"
    assert item5.condition_description()=="perfect"
    
