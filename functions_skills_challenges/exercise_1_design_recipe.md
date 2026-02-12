
## 1. Describe the Problem

> As a user\
So that I can manage my time\
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._
Function name: time_management()
parameters: string
return value: int

```python
# EXAMPLE

def time_estimation(sample):
    """Calculates estimated reading time

    Parameters: (list all parameters and their types)
        mixed_words: a string containing words (e.g. "hello world")

    Returns: (state the return value and its type)
        an f"" value (e.g. f"it will take {10} minutes to read this doc")

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It returns 0 min
"""
time_estimation("") => 0 min

"""
Given a string 10 words long
It returns ETR
"""
time_estimation("HELLO" x 10) => .05 min

"""
Given a string 100 words long
It returns ETR
"""
time_estimation("hello" * 100) => .5 min

"""
Given a string 200 words long
It returns ETR
"""
time_estimation("hello ") => []

"""
Given a lowercase word and an uppercase word with an exclamation mark
It returns a list with the uppercase word, no exclamation mark
"""
time_estimation("hello WORLD!") => ["WORLD"]

"""
Given an empty string
It returns an empty list
"""
extract_uppercase("") => []

"""
Given a None value
It throws an error
"""
extract_uppercase(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
