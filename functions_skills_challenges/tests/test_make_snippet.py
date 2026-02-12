from lib.make_snippet import make_snippet

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
