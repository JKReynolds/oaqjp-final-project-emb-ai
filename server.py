from flask import Flask
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)
    anger, disgust, fear, joy, sadness, dominant_emotion = (
        result['anger'],
        result['disgust'],
        result['fear'],
        result['joy'],
        result['sadness'],
        result['dominant_emotion']
    )

    response = (
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and "
        f"'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    if dominant_emotion is None:
        return "Invalid, try again"
    return response

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000)