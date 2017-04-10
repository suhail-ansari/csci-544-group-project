import markovify
import csv
import nltk
import re
import pickle
import sys
from pos_text import POSText


state_size = 2
if len(sys.argv) > 1:
  lang = sys.argv[1]
  if len(sys.argv) > 2:
    state_size = int(sys.argv[2])
else:
  lang = 'es'

with open('tagger.%s.pickle' % lang, 'rb') as f:
  tagger = pickle.load(f)

csvpaths = ['../espnus.csv'] if lang == 'en' else ['../as.csv', '../espn.csv']
text = []
for csvpath in csvpaths:
  with open(csvpath, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      text.append(row['text'].rstrip('.') + '.')

print('training model lang=%s state_size=%d ...' % (lang, state_size))
text_model = POSText('\n'.join(text), state_size=state_size, tagger=tagger)

with open('%s-%d.model' % (lang, state_size), 'wb') as f:
  pickle.dump(text_model, f)