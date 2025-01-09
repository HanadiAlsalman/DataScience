from uppgift_6 import multiplication_tabellen

def test_funktion():
    assert multiplication_tabellen(2, 3) == [2, 4, 6]
    assert multiplication_tabellen(3, 5) == [3, 6, 9, 12, 15]


