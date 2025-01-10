from uppgift_10 import celsicus_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert celsicus_to_fahrenheit(0) == 32
    assert celsicus_to_fahrenheit(100) == 212
    assert celsicus_to_fahrenheit(-40) == -40
