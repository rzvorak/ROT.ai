from flask import Flask, request, jsonify
from GoogleCurrent import cur  
from GoogleINFO4months import fourMonths
from GoogleInfoMaxTo30AfterDecimal import max
from GoogleInfoMinTo30AfterDecimal import min
from RedditAPI import testRedditAPI
from pronunciation import get_pronunciation_score, prevalenceScore
import torch
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load model once to avoid reloading for each request
model = torch.load('rot_model.pth', map_location=torch.device('cpu'))
model.eval()

# Create an endpoint that accepts POST requests with a word input
@app.route('/get-trend', methods=['POST'])
def gettrend():
    # Get the word from the incoming JSON request
    data = request.get_json()
    word = data.get('word')

    if not word:
        return jsonify({"error": "No word provided"}), 400

    # Get the trend value using the cur() function
    curVal = cur(word)
    fourMonth = fourMonths(word)
    wordMax = max(word)
    wordMin = min(word)
    red = testRedditAPI(word)

    # Get pronunciation and prevalence score
    pron = get_pronunciation_score(word)
    prev = prevalenceScore(pron)

    # Create a vector with the gathered data
    vector = red + [wordMin, wordMax, fourMonth, prev]

    try:
        # Convert the vector to numpy array and reshape it to (1, 5)
        dvector = np.array(vector, dtype=np.float32).reshape(1, 5)

        # Convert numpy array to torch tensor
        tensor_input = torch.tensor(dvector)

        # Run the model on the input
        with torch.no_grad():  # No need to track gradients for inference
            output = model(tensor_input)

        # Return the output as a JSON response
        return jsonify({"output": output.tolist()})  # Convert tensor to list for JSON serialization

    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, port=5000)  # You can change the port if needed