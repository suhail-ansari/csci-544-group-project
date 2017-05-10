# csci-544-group-project
Repo for the CSCI 544 Spring 2017 group project

## Markovify
Sentence generation using markov chain.

### Usage
```bash
cd markovify
```
Generate a POS tagger for each language (es/en). Requires `nltk` with `brown` and `cess_esp` corpus.
```bash
# usage: python3 train_tagger.py [lang=es]
python3 train_tagger.py es
python3 train_tagger.py en
```
Train the models. *This will take about 20 minutes for each model on 1.8 GHz Intel Core i5 (MacBook Air Mid 2012).*
```bash
# usage: python3 train_tagger.py [lang=es] [state_size=2]
python3 train_model es 2
python3 train_model en 2
```
Run the web server.
```bash
python3 webserver.py
```
To get a generated sentence, go to the url ``http://127.0.0.1:5000`` for Spanish commentary or ``http://127.0.0.1:5000/es`` for English.

## RNN

To run the RNN based sentence generator:
```bash
python RNN -i RNN/as_com.csv -s
```
This will start training the model if there does not exists a file named ``rnn_model.h5`` in RNN folder and start a web server after the best model is found. You can generate a sentence by going to ``http://127.0.0.1:5000/`` or `` http://127.0.0.1:5000/(length)``.
