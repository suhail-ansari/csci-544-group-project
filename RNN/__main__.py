import argparse
import csv
import os

from flask import Flask, request, send_from_directory

from RNN import RNN

if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('-i', '--input', type=str, help="input csv")
    argument_parser.add_argument('-s', '--server', action='store_true')

    args = argument_parser.parse_args()

    print args

    with open(args.input, 'r') as input_csv:
        text = " ".join([i[0] for i in list(csv.reader(input_csv))[1:]]).lower()
        
        rnn = RNN(text)
        rnn.make_pattern()
        rnn.make_model()

        if os.path.exists('./RNN/rnn_model.h5'):
            rnn.load_model('./RNN/rnn_model.h5')
        else:
            rnn.calculate_weights()
        

        if args.server:
            app = Flask(__name__)

            @app.route('/')
            def index():
                seed, sentence = rnn.make_sentence(50)
                return '{"seed":%s, "out":%s}'%(seed, sentence)

            app.run(port=5000, host='0.0.0.0')

        #seed, sentence = rnn.make_sentence()
        #print "Seed:{}\nOut:{}".format(seed, sentence)

            
        
