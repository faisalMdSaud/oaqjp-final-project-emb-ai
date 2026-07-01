from flask import Flask, render_template, request 
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def detect_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response_dict = emotion_detector(text_to_analyze)
    output_sentence = (
        f"For the given statement, the system response is "
        f"'anger': {response_dict['anger']}, 'disgust': {response_dict['disgust']}, "
        f"'fear': {response_dict['fear']}, 'joy': {response_dict['joy']} and "
        f"'sadness': {response_dict['sadness']}. "
        f"The dominant emotion is {response_dict['dominant_emotion']}."
    )
    
    return output_sentence


    
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)