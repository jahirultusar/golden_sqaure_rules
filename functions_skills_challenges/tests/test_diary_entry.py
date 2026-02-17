
from lib.diary_entry import DiaryEntry

def test_checks_the_initial_state_of_the_object():
    # 1 Checks the initial state of the object
    entry = DiaryEntry("Sample Title", "Sample Contents do re mi..")
    assert entry.title == "Sample Title"
    assert entry.contents == "Sample Contents do re mi.."

def test_checks_the_state_of_a_formatted_diary():
    # 2 Returns a formatted diary entry
    entry = DiaryEntry("Hello", "World!")
    assert entry.format() == "Hello: World!"

def test_returns_the_word_count():
    # 3 Returns the total word count
    entry = DiaryEntry("any", "any " * 2)
    assert entry.count_words() == 2 

def test_returns_estimated_reading_time():
    """ 4 Returns estimated reading time"""
    content = " ".join(["word" for _ in range(200)])
    entry = DiaryEntry("title ", content)
    assert entry.time_estimation(200) == 1


def test_returns_first_reading_chunks():
    """ #5: Docstring for test_returns_reading_chunks"""
    entry = DiaryEntry("title ", "one two three")
    assert entry.reading_chunks(3, 1) == "one two three"
    

def test_returns_first_reading_chunks_2():
    """ #5: Docstring for test_returns_reading_chunks"""
    entry = DiaryEntry("title ", "one two three four five six")
    assert entry.reading_chunks(5, 2) == "one two three four five six"