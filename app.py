# Digital OCEAN FLASK SERVER RECEIVES IMAGE
from flask import Flask, request, jsonify
import classify
import base64
import os
import gc

import json
import firebase
import env
from classify import init

# Instantiate Flask
app = Flask(__name__)


# health check
@app.route('/status')
def health_check():
    return 'Running!'


# Performing image Recognition on Image, sent as bytes via POST payload
@app.route('/detect', methods=["POST"])
def detect():
    gc.collect()
    imgBytes = request.data

    imgdata = base64.b64decode(imgBytes)
    with open("temp.png", 'wb') as f:
        f.write(imgdata)
    f.close()
    print("successfully receieved image")
    
    # Pass image bytes to classifier
    result = classify.analyse("temp.png")
	
    # Return results as neat JSON object, using 
    result = jsonify(result)
    print(result.json)

    response_data = result.json
    
    return response_data
if __name__ == '__main__':
    init()
    try:
        port = os.environ['PORT']
    except:
        port = "8080"

    app.run(host='0.0.0.0', port=port, debug=True)

