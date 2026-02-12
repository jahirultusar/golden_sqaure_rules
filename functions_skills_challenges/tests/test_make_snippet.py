from lib.make_snippet import make_snippet, count_words

"""
smoke test: A function called make_snippet
that takes a string as an argument

"""
# def test_function_called_make_snippet():
#     function = make_snippet("text")


"""
Funtion will return when exactly five words
"""    
def test_function_will_return_five_words():
    function = make_snippet("one two three four five")
    assert function == "one two three four five"

"""
Test returns four words without dots
"""
def test_returns_four_words_without_dots():
    function = make_snippet("one two three four")
    assert function == "one two three four"

"""
Test returns six words with dots
"""
def test_returns_six_words_with_dots():
    function = make_snippet("one two three four five six")
    assert function == "one two three four five ..."

#================ count_words funtion tests below =================

def test_returns_zero_for_empty_string():
    """It should return 0 if empty string"""
    assert count_words("") == 0

def test_three_for_three_words():
    """It should return 3 for 'one, two, three'"""
    assert count_words('one, two, three') == 3

def test_handles_extra_whitespace():
    """It should ignore the whitespace and return 2 for 'Hello   World'"""
    assert count_words('Hello   World') == 2