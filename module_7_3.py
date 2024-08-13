class WordsFinder:
  def __init__(self, *file_names):
    self.file_names = file_names

  def get_all_words(self):
    all_words = {}
    for file_name in self.file_names:
      with open(file_name, 'r', encoding='utf-8') as file:
        t = file.read().lower()
        for znaki in [',', '.', '=', '!', '?', ';', ':', ' - ']:
          t = t.replace(znaki, '')
        words = t.split()
        all_words[file] = words
    return all_words


  def find(self, word):
    all_words = self.get_all_words()
    dict = {}
    for file_name, words in all_words.items():
      if word.lower() in words:
        index = words.index(word.lower()) + 1
        dict[file_name] = index
      return dict
      

  def count(self, word):
    all_words = self.get_all_words()
    dict = {}
    for file_name, words in all_words.items():
      count = words.count(word.lower())
      if count > 0:
        dict[file_name] = count
    return dict




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
