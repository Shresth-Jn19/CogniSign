from flask import Flask, request, jsonify
import cv2
import numpy as np
# Import necessary modules and functions

app = Flask(__name__)

@app.route('/process_frame', methods=['POST'])
def process_frame():
    # Assume a frame is sent as a file in a multipart-form request
    file = request.files['frame'].read()
    # Convert string data to numpy array
    nparr = np.fromstring(file, np.uint8)
    # Decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Here you can process the image/frame with OpenCV and Mediapipe
    
    # For simplicity, let's just return a JSON saying processing was done
    return jsonify({"message": "Frame processed"}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)
