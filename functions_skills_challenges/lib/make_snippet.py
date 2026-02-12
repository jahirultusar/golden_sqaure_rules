# Skills challenge - Functions

# to get the first five words: words.split()[:5]

def make_snippet(sample):
    all_words = sample.split()
    splited_word_list =  all_words[:5]
    if len(all_words) <= 5:
        return sample
    else:
        return " ".join(splited_word_list) + " ..."
