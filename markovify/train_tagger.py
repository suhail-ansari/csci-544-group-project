import nltk
import sys
import pickle


tagger = nltk.tag.tnt.TnT()
if len(sys.argv) > 1:
  lang = sys.argv[1]
else:
  lang = 'es'

if lang == 'en':
  tagger.train(nltk.corpus.brown.tagged_sents())
else:
  tagger.train(nltk.corpus.cess_esp.tagged_sents())

with open('tagger.%s.pickle'%(lang), 'wb') as f:
  pickle.dump(tagger, f)