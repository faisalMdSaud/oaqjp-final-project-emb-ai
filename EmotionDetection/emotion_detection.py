import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputObj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputObj, headers = headers)
    

    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        # 1. Unpack the list to isolate the target emotions dictionary
        [prediction_details] = formatted_response['emotionPredictions']
        emotions_dict = prediction_details['emotion']
        # 2. Find the name of the dominant emotion
        dominant_name = max(emotions_dict, key=emotions_dict.get)
        # 3. Construct the output in your requested dictionary format
        result = {
            'anger': emotions_dict['anger'],
            'disgust': emotions_dict['disgust'],
            'fear': emotions_dict['fear'],
            'joy': emotions_dict['joy'],
            'sadness': emotions_dict['sadness'],
            'dominant_emotion': dominant_name
        }
        # Print the final result
        print(result)

    



        # label = formatted_response['documentSentiment']['label']
        # score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None
    else:
        label = None
        score = None
   

    # if response.status_code == 200:

    # from emotion_detection import emotion_detector
    # emotion_detector("I love this new technology.")