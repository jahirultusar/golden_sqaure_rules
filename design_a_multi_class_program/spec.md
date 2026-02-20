# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

>As a user
So that I can record my experiences
I want to keep a regular diary

>As a user
So that I can reflect on my experiences
I want to read my past diary entries

>As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

>As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

>As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries



## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
> In this architecture, the Diary and TodoList act as Containers (the "Orchestrators") that hold lists of smaller Data objects (DiaryEntry and Todo)

┌──────────────────────────────┐      ┌──────────────────────────────┐
│ Diary                        │      │ DiaryEntry                   │
│                              │      │                              │
│ - entries: [DiaryEntry]      │      │ - title: string              │
│                              │      │ - contents: string           │
│ + add(entry)                 │      │                              │
│ + all()                      │◀─────┤ + count_words()              │
│ + find_best_entry(...)       │ owns │ + reading_time(wpm)          │
│ + list_phone_numbers()       │      │ + reading_chunk(wpm, mins)   │
└──────────────────────────────┘      └──────────────────────────────┘

┌──────────────────────────────┐      ┌──────────────────────────────┐
│ TodoList                     │      │ Todo                         │
│                              │      │                              │
│ - todos: [Todo]              │      │ - task: string               │
│                              │      │ - complete: boolean          │
│ + add(todo)                  │◀─────┤                              │
│ + incomplete()               │ owns │ + mark_complete()            │
│ + complete()                 │      │                              │
│ + give_up()                  │      │                              │
└──────────────────────────────┘      └──────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python

# File: lib/diary.py

class Diary:
    # Diary and Todos
    def __init__(self):
        pass

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        pass

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        pass

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        pass

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        pass
    
    def list_phone_numbers(self):
        # Returns:
        #   A list of strings representing unique 11-digit phone numbers 
        #   found across all diary entries.
        pass


# File: lib/diary_entry.py

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        pass

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        pass

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        pass

# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

####### 
```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python

# TODO unittests

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

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
