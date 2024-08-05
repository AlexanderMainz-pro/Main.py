def single_root_words(root_word, *other_words):
    same_words = []
    for root_word in other_words:
        same_words = root_word
        return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)