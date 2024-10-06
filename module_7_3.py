import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    content = file.read().lower()
                    translator = str.maketrans('', '', string.punctuation.replace('-', ''))
                    content = content.translate(translator)
                    words = content.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
                all_words[file_name] = []
        return all_words

    def find(self, word):
        results = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for name, words in all_words.items():
            if word_lower in (w.lower() for w in words):
                results[name] = next(i for i, w in enumerate(words) if w.lower() == word_lower)
            return results

    def count(self, word):
        results = {}
        all_words = self.get_all_words()
        word_lower = word.lower()
        for name, words in all_words.items():
             results[name] = sum(1 for w in words if w.lower() == word_lower)
        return results


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего