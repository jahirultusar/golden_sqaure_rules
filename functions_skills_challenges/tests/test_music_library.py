    
from lib.music_library import MusicLibrary

def test_returns_empty_list():
    """Initially, searching returns an empty list"""
    library = MusicLibrary()

    assert library.search("Any track") == []


def test_returns_any_track_that_added():
    """When we add a track, it appears in the search results for that track"""
    library = MusicLibrary()
    library.add("Higher Love")
    
    assert library.search("Higher Love") == ["Higher Love"]

def test_returns_any_track_that_added():
    """When we add a track, it appears in the search results for that track"""
    library = MusicLibrary()
    library.add("Tomb. raider")
    
    assert library.search("") == ["Tomb. raider"]

def test_returns_that_matches_keyword():
    """
    When we add multiple tracks, searching returns only the ones that match
    """
    library = MusicLibrary()
    library.add("Higher Love")
    library.add("Stairway to Heaven")
    assert library.search("Love") == ["Higher Love"]