from flask import Flask, render_template
import pickle


models = {}

with open('es-2.model', 'rb') as f:
  models['es'] = pickle.load(f)

with open('en-2.model', 'rb') as f:
  models['en'] = pickle.load(f)

app = Flask(__name__, template_folder=".")

@app.route('/')
@app.route('/<lang>')
@app.route('/<lang>/<int:tries>')
def index(lang='es', tries=10):
  print('markov lang=%s tries=%d' % (lang, tries))
  sentence = models[lang].make_sentence(tries=tries) or ''
  return render_template('index.html', sentence=sentence)

app.run(port=5001, host='0.0.0.0')
