from flask import Flask
import pickle


models = {}

with open('es-2.model', 'rb') as f:
  models['es'] = pickle.load(f)

with open('en-2.model', 'rb') as f:
  models['en'] = pickle.load(f)

app = Flask(__name__)

@app.route('/')
@app.route('/<lang>')
@app.route('/<lang>/<int:tries>')
def index(lang='es', tries=10):
  print('markov lang=%s tries=%d' % (lang, tries))
  return models[lang].make_sentence(tries=tries) or ''

app.run()
