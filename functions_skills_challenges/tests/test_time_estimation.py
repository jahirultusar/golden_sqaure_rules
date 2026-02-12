from lib.time_estimation import time_estimation


"""
Given an empty string
It returns 0 min
"""
def test_returns_0_mins():
    assert time_estimation("") == "0 minutes, 0 seconds"

"""
Given an 10 words string
It returns 10 min
"""
def test_returns_mins():
    words = "test " * 10
    assert time_estimation(words) == "0 minutes, 3 seconds"

def test_returns_etr_for_100_words():
    words = "test " * 100
    assert time_estimation(words) == "0 minutes, 30 seconds"

def test_returns_etr_for_1000_words():
    words = "test " * 1000
    assert time_estimation(words) == "5 minutes, 0 seconds"

def test_returns_etr_for_3500_words():
    words = "test " * 3500
    assert time_estimation(words) == "17 minutes, 30 seconds"