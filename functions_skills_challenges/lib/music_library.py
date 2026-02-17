"""
Clarifying Notes:
- We need a MusicLibrary class.
- It should store a list of track titles (strings).
- It needs a method to add a track.
- It needs a method to search and return tracks that match a keyword.
"""

class MusicLibrary:
    
    def __init__(self):
        self._list = []
    
    def add(self, track):
        if isinstance(track, str):
            self._list.append(track)

    def search(self, keyword):
        results = []
        for track in self._list:
            if keyword in track:
                results.append(track)
        return results
