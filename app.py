from PIL import Image
from flask import Flask, request, jsonify
from io import BytesIO
import classify

# Instantiate Flask
app = Flask(__name__)


# health check
@app.route('/status')
def health_check():
    return 'Running!'


# Performing image Recognition on Image, sent as bytes via POST payload
@app.route('/detect', methods=["POST"])
def detect():
    try:
        # Converts bytes, received via request, to Pillow Image Object
        pil_img = Image.open(BytesIO(request.data))

        # Pass image bytes to classifier
        result = classify.analyse(pil_img)
    
        # Return results as neat JSON object, using 
        result = jsonify(result)
        print(result)
        return result
    
    except:
        return jsonify(
            {
                "Error": "Image could not be read and/or parsed."
            }
        )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
