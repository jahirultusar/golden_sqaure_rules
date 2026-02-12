
def time_estimation(sample):
    total_words = sample.split()
    word_count = len(total_words)
    total_seconds = int(word_count * (60 / 200))
    minutes, seconds = divmod(total_seconds, 60)

    return f"{minutes} minutes, {seconds} seconds"