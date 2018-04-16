import MeCab
import sys
import math


class NaiveBayes:

    def __init__(self):
        self.vocabularies = set()
        self.word_count = {}
        self.category_count = {}

    def train(self, document, category):
        m = MeCab.Tagger("-Owakati")
        word_list = m.parse(document).split()

        for word in word_list:
            self.__word_count_up(word, category)

        self.__category_count_up(category)

    def __word_count_up(self, word, category):

        self.word_count.setdefault(category, {})

        self.word_count[category].setdefault(word, 0)

        self.word_count[category][word] += 1

        self.vocabularies.add(word)

    def __category_count_up(self, category):
        self.category_count.setdefault(category, 0)

        self.category_count[category] += 1

    def classifier(self, document):
        best_category = None
        max_prob = -sys.maxsize

        m = MeCab.Tagger("-Owakati")
        word_list = m.parse(document).split()

        for category in self.category_count.keys():
            prob = self.__score(word_list, category)
            if prob > max_prob:
                max_prob = prob
                best_category = category
        return best_category

    def __score(self, word_list, category):
        score = math.log(self.__prior_prob(category))
        for word in word_list:
            score += math.log(self.__word_prob(word, category))
        return score

    def __prior_prob(self, category):
        return float(self.category_count[category] / sum(self.category_count.values()))

    def __word_prob(self, word, category):
        prob = (self.__in_category(word, category) + 1.0)/(sum(self.word_count[category].values()) + len(self.vocabularies) * 1.0)

        return prob

    def __in_category(self, word, category):
        if word in self.word_count[category]:
            return float(self.word_count[category][word])
        return 0.0
