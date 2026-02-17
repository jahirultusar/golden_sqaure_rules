
class DiaryEntry:
    def __init__(self, title, contetnts):
        """Initializes the objects"""
        self.title = title
        self.contents = contetnts
        self.read_pointer = 0
    
    def format(self):
        """Formats the title and contents"""
        return f"{self.title}: {self.contents}"

    def count_words(self):
        """Returns the number of words in the entry contents"""
        total_words = self.contents.split()
        return len(total_words)
    
    def time_estimation(self, wpm):
        wpm = self.count_words() / 200
        return int(wpm)
    
    def reading_chunks(self, wpm, minutes):
        words = self.contents.split()
        # words_to_read = self.count_words()
        words_to_read = wpm * minutes
        start = self.read_pointer
        end = start + words_to_read
        chunk_words = words[start:end]

        self.read_pointer = end
        
        if self.read_pointer >= len(words):
            self.read_pointer = 0
        
        return " ".join(chunk_words)
 
# class DiaryEntry:
    # def __init__(self, title, contents):
    #     # Parameters:
    #     #   title: string
    #     #   contents: string
    #     pass

    # def format(self):
    #     # Returns:
    #     #   A formatted diary entry, for example:
    #     #   "My Title: These are the contents"
    #     pass

    # def count_words(self):
    #     # Returns:
    #     #   int: the number of words in the diary entry
    #     pass

    # def reading_time(self, wpm):
    #     # Parameters:
    #     #   wpm: an integer representing the number of words the user can read 
    #     #        per minute
    #     # Returns:
    #     #   int: an estimate of the reading time in minutes for the contents at
    #     #        the given wpm.
    #     pass

    # def reading_chunk(self, wpm, minutes):
    #     # Parameters
    #     #   wpm: an integer representing the number of words the user can read
    #     #        per minute
    #     #   minutes: an integer representing the number of minutes the user has
    #     #            to read
    #     # Returns:
    #     #   string: a chunk of the contents that the user could read in the
    #     #           given number of minutes
    #     #
    #     # If called again, `reading_chunk` should return the next chunk,
    #     # skipping what has already been read, until the contents is fully read.
    #     # The next call after that should restart from the beginning.
    #     pass
