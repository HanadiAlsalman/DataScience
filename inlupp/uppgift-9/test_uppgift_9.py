from uppgift_9 import is_palimdrome

def test_is_palindrome():
    assert is_palimdrome("radar") == True
    assert is_palimdrome("python") == False
    assert is_palimdrome("") == True


