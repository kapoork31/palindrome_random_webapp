from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import logging
import traceback
from src.utils import gen_random_string
import numpy as np

def create_app():
    """
    function to create API
    create a function like so so testing with pytest is seamless experience
    """
    app = Flask(__name__)
    logging.basicConfig(filename='record.log', level=logging.DEBUG)
    # enable logging to record.log files for successes/warnings/errors on endpoint requests

    CORS(app)
    # cors added to so js code on webpage could access the endpoint

    @app.route("/random_gen_endpoint", methods=['POST'])
    def random_gen_endpoint():
        """
        Read in data from request
        check if data is only alpha numerics
            if so then generate random string format and return
            else return message asking for only alphanumeric characters
        """
        try:
            data = request.json
            string_message = data['message']

            if not string_message.isalnum():
                return jsonify({'message':'please only enter alphabetic characters'})

            rnd_int = np.random.randint(11,size =1)[0]
            random_string = gen_random_string(string_message,rnd_int)
            message = {'message':random_string}
            return jsonify(message)
        except Exception as e:
            logging.error(traceback.format_exc())
            message = {'message':'error has occured'}
            return jsonify(message)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0')