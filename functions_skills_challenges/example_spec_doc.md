
## 1. Describe the Problem

> As a user\
So that I can find my tasks among all my notes\
I want to check if a line from my notes includes the string `#TODO`.

## 2. Design the Function Signature

```python
# EXAMPLE

def includes_todo(line):
    """Extracts lines containing the string `#TODO`

    Parameters: (list all parameters and their types)
        line: a string type

    Returns: (state the return value and its type)
        True if a line contains `#TODO`
        False if a line does not contain `#TODO`

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

```python
# EXAMPLE

"""
Test is a line does not contain `#TODO`
Expected output should be False
"""
line_example = includes_todo("Buy groceries")
line_eample == False

"""
Test if a line starts with `#TODO`
Expected output should be True
"""
line_example = includes_todo("#TODO Buy groceries")
line_eample == True

"""
Test if a line ends with `#TODO`
Expected output should be True
"""
line_example = includes_todo("Buy groceries #TODO")
line_eample == True


"""
Test with a line containing #TODO with punctuation - e.g. #TODO:
Expected output should be True
"""

line_example = includes_todo("#TODO: Buy groceries")
line_eample == True

"""
Test with lower case #todo
Expected output should be True
"""
line_example = includes_todo("#todo: Buy groceries")
line_eample == True

"""
Test withouth the hash symbol - e.g. TODO
Expected output should be False
"""

line_example = includes_todo("TODO Buy groceries")
line_eample == False

