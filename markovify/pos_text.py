import markovify
import re


class POSText(markovify.Text):
  def __init__(self, *args, **kwargs):
    self.tagger = kwargs.pop('tagger', None)
    super(POSText, self).__init__(*args, **kwargs)

  def test_sentence_input(self, sentence):
    return True

  def word_split(self, sentence):
    words = re.split(self.word_split_pattern, sentence.lower())
    words = ['::'.join(tag) for tag in self.tagger.tag(words)]
    return words

  def word_join(self, words):
    sentence = ' '.join(word.split('::')[0] for word in words)
    return sentence
