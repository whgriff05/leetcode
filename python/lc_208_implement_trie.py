class Trie:


    def __init__(self):
        self.prefixes = {}
        self.words = {}


    def insert(self, word):
        if word in self.words:
            self.words[word] += 1
        else:
            self.words[word] = 1

        for i in range(len(word)):
            tp = word[0:(i+1)]
            if tp in self.prefixes:
                self.prefixes[tp] += 1
            else:
                self.prefixes[tp] = 1


    def search(self, word):
        if word in self.words:
            return True
        return False


    def startsWith(self, prefix):
        if prefix in self.prefixes:
            return True
        return False


# Tests
from testsuite import lc_test

trie = Trie()
trie.insert("apple")

lc_test(1, trie.search("apple"), True)
lc_test(2, trie.search("app"), False)
lc_test(3, trie.startsWith("app"), True)

trie.insert("app")
lc_test(4, trie.search("app"), True)


