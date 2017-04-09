# csci-544-group-project
Repo for the CSCI 544 Spring 2017 group project

## Markovify
Sentence generation using markov chain.

### Usage
```bash
cd markovify
```
Generate a POS tagger for each language (es/en).
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
