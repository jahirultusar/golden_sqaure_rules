
"""
Docstring for design_a_single_class_program.tests.test_todo
"""

import pytest
from lib.todo import ToDo

def test_returns_empty_todo_list():
    """Checks an empty list"""
    object = ToDo()
    assert object.todo_list == []

def test_returns_one_task_when_added():
    """returns with one added task """
    object = ToDo()
    object.add("Drink water")
    assert object.todo_list == ["Drink water"]

def test_checks_if_to_do_is_string():
    """returns error if not """
    object = ToDo()
    with pytest.raises(TypeError, match="Entry should be string only"):
            object.add(5)

def test_():
    """returns updated list with completed task"""
    object = ToDo()

    object.add("Drink water")
    object.add("Go to gym")
    object.add("Check tyre")

    with pytest.raises(ValueError, match="No task found!"):
        object.complete("Drink waater")