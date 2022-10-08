"""
test utils functions of palindrome and gen_random_string
"""

from src.utils import palindrome, gen_random_string

def test_palindrome_true_even_length():
    assert palindrome('toooot') == True

def test_palindrome_true_odd_length():
    assert palindrome('toosoot') == True

def test_palindrome_false_even_length():
    assert palindrome('sfsdffds') == False

def test_palindrome_false_odd_length():
    assert palindrome('sdfsdfo') == False

def test_palindrome_false_odd_length():
    assert palindrome('sdfsdfo') == False

def test_palindrome_one_letter():
    assert palindrome('a') == True

def test_gen_random_string_not_a_palindrome():
    message = 'elephant'
    rnd_int = 4
    result = 'I would like {} {} please. {} is not a palindrome'.format(rnd_int, message, message)
    assert result == gen_random_string(message,rnd_int)

def test_gen_random_string_palindrome():
    message = 'foofoof'
    rnd_int = 4
    result = 'I would like {} {} please. {} is a palindrome'.format(rnd_int, message, message)
    assert result == gen_random_string(message,rnd_int)
