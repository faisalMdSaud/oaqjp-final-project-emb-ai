"""Flask server for the Emotion Detection web application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


APP = Flask("Emotion Detection")
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 5000


def format_emotion_response(response_dict):
    """Format the emotion detector response into a user-readable string."""
    return (
        "For the given statement, the system response is "
        f"'anger': {response_dict['anger']}, "
        f"'disgust': {response_dict['disgust']}, "
        f"'fear': {response_dict['fear']}, "
        f"'joy': {response_dict['joy']} and "
        f"'sadness': {response_dict['sadness']}. "
        f"The dominant emotion is {response_dict['dominant_emotion']}."
    )


@APP.route("/emotionDetector")
def detect_emotion():
    """Analyze the submitted text and return the detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    response_dict = emotion_detector(text_to_analyze)

    if response_dict["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return format_emotion_response(response_dict)


@APP.route("/")
def render_index_page():
    """Render the home page."""
    return render_template("index.html")


if __name__ == "__main__":
    APP.run(host=SERVER_HOST, port=SERVER_PORT)