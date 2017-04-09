import pickle
import sys


state_size = 2
if len(sys.argv) > 1:
  lang = sys.argv[1]
  if len(sys.argv) > 2:
    state_size = int(sys.argv[2])
else:
  lang = 'es'

with open('%s-%d.model' % (lang, state_size), 'rb') as f:
  text_model = pickle.load(f)

for i in range(20):
  print(i, text_model.make_sentence(tries=10))
