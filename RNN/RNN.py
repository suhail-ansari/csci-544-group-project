import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import kutils

import sys

class RNN:
    def __init__(self, text):
        self.text = text
        
        self.unique_chars = sorted(list(set(text)))
        self.charmap = {c: i for i, c in enumerate(self.unique_chars)}
        self.intmap = {i: c for i, c in enumerate(self.unique_chars)}

        self.text_len = len(text)
        self.char_num = len(self.unique_chars)
        
    def make_pattern(self, sequence_len=100):
        
        dX = []
        dY = []

        for i in range(0, self.text_len - sequence_len, 1):
            sequence_in = self.text[i:i + sequence_len]
            sequence_out = self.text[i + sequence_len]
            dX.append([self.charmap[char] for char in sequence_in])
            dY.append(self.charmap[sequence_out])
        pattern_num = len(dX)
        
        X = numpy.reshape(dX, (pattern_num, sequence_len, 1))
        X = X / float(self.char_num)
        
        y = kutils.to_categorical(dY)

        self.dX = dX
        self.dY = dY
        self.X = X
        self.y = y
    
    def make_model(self):
        self.model = Sequential()
        self.model.add(LSTM(256, input_shape=(self.X.shape[1], self.X.shape[2])))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(self.y.shape[1], activation='softmax'))
        self.model.compile(loss='categorical_crossentropy', optimizer='adam')

    def calculate_weights(self, filepath="rnn_model.hdf5"):
        filepath = "rnn_model_{epoch}_{loss}.h5"
        checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
        callbacks_list = [checkpoint]
        self.model.fit(self.X, self.y, epochs=50, batch_size=64, callbacks=callbacks_list)

    def load_model(self, filepath="rnn_model.hdf5"):
        if not self.model:
            self.make_model()
        
        self.model.load_weights(filepath)
        self.model.compile(loss='categorical_crossentropy', optimizer='adam')
    
    def make_sentence(self, sequence_len=30):
        start = numpy.random.randint(0, len(self.dX)-1)
        start_pattern = self.dX[start]
        seed_sequence = ''.join([self.intmap[value] for value in start_pattern]) 
        res = ""
        for i in range(sequence_len):
            x = numpy.reshape(start_pattern, (1, len(start_pattern), 1))
            x = x / float(self.char_num)
            prediction = self.model.predict(x, verbose=0)
            index = numpy.argmax(prediction)
            result = self.intmap[index]
            res += result
            start_pattern.append(index)
            start_pattern = start_pattern[1:len(start_pattern)]
        return seed_sequence, res
        
        