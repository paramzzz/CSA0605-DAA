class WordFilter:
    def __init__(self, words):
        self.prefix_dict = {}
        self.suffix_dict = {}
        for i, word in enumerate(words):
            for j in range(len(word)):
                prefix = word[:j+1]
                suffix = word[j:]
                if prefix not in self.prefix_dict:
                    self.prefix_dict[prefix] = set()
                if suffix not in self.suffix_dict:
                    self.suffix_dict[suffix] = set()
                self.prefix_dict[prefix].add(i)
                self.suffix_dict[suffix].add(i)

    def f(self, pref, suff):
        pref_set = self.prefix_dict.get(pref, set())
        suff_set = self.suffix_dict.get(suff, set())
        common_set = pref_set & suff_set
        return max(common_set) if common_set else -1

words = ["apple", "banana", "app", "appl", "ap", "bat", "batman"]
wordFilter = WordFilter(words)
print(wordFilter.f("ap", "le"))  # Output: 0
print(wordFilter.f("ba", "na"))  # Output: 1
print(wordFilter.f("bat", "man"))  # Output: 5
