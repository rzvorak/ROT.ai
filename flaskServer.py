from flask import Flask, request, jsonify
from GoogleCurrent import cur  
from GoogleINFO4months import fourMonths
from GoogleInfoMaxTo30AfterDecimal import max
from GoogleInfoMinTo30AfterDecimal import min
from RedditAPI import testRedditAPI
from pronunciation import get_pronunciation_score, prevalenceScore

#Initialize Flask app
app = Flask(__name__)

#Create an endpoint that accepts POST requests with a word input
@app.route('/get-trend', methods=['POST'])
def gettrend():
    word = "test"

    # Get the trend value using the cur() function
    curVal = cur(word)

    fourMonth = fourMonths(word)
    wordMax = max(word)
    wordMin = min(word)
    red = testRedditAPI(word)

    pron = get_pronunciation_score(word)
    prev = prevalenceScore(pron)

    vector = red + [wordMin, wordMax, fourMonth, prev]

#Run the Flask app
if __name__ == '__main':
    app.run(debug=True, port=5000)  # You can change the port if needed