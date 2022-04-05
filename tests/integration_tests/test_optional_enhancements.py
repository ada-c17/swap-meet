import pytest
from swap_meet.vendor import Vendor
from swap_meet.clothing import Clothing
from swap_meet.decor import Decor
from swap_meet.electronics import Electronics

def test_integration_optional_enhancements():
    
    

    camila = Vendor()
    valentina = Vendor()

    item_clothing1 = Clothing(condition=1.0, age=1)
    item_clothing2 = Clothing(condition=2.0)
    item_electronics1 = Electronics(condition=1.0, age=2.5)
    item_electronics2 = Electronics(condition=2.0, age=3.1)
    item_decor1 = Decor(condition=1.0, age=0.4)
    item_decor2 = Decor(condition=2.0)

    camila.add(item_electronics1)
    camila.add(item_clothing1)
    camila.add(item_clothing2)

    valentina.add(item_electronics2)
    valentina.add(item_decor1)
    valentina.add(item_decor2)
    
    # swap_by_newest - truthy
    result = camila.swap_by_newest(valentina)
    
    assert result
    assert len(camila.inventory) == 3
    assert item_electronics1 in camila.inventory
    assert item_clothing2 in camila.inventory
    assert item_decor1 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics2 in valentina.inventory
    assert item_decor2 in valentina.inventory
    assert item_clothing1 in valentina.inventory


    # camila now has item_electronics1, item_clothing2, item_decor1
    # valentina now has item_electronics2, item_clothing1, item_decor2

    # swap_best_category - truthy

    result = camila.swap_best_by_category(valentina, "Decor", "Clothing")

    assert result
    assert len(camila.inventory) == 3
    assert item_electronics1 in camila.inventory
    assert item_decor1 in camila.inventory
    assert item_decor2 in camila.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics2 in valentina.inventory
    assert item_clothing1 in valentina.inventory
    assert item_clothing2 in valentina.inventory


    # swap_by_newest - falsy

    john = Vendor()
    jill = Vendor()

    item_clothing1 = Clothing(condition=1.0)
    item_clothing2 = Clothing(condition=2.0)
    item_electronics1 = Electronics(condition=1.0)
    item_electronics2 = Electronics(condition=2.0)
    item_decor1 = Decor(condition=1.0, age=0.4)
    item_decor2 = Decor(condition=2.0)

    john.add(item_electronics1)
    john.add(item_clothing1)
    john.add(item_clothing2)

    jill.add(item_electronics2)
    jill.add(item_decor1)
    jill.add(item_decor2)

    result = john.swap_by_newest(jill)

    assert not result
    assert len(john.inventory) == 3
    assert item_electronics1 in john.inventory
    assert item_clothing1 in john.inventory
    assert item_clothing2 in john.inventory

    assert len(valentina.inventory) == 3
    assert item_electronics2 in jill.inventory
    assert item_decor1 in jill.inventory
    assert item_decor2 in jill.inventory

