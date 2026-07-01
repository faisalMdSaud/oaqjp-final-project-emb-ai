import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    inputObj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = inputObj, headers = headers)
    
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        print(formatted_response)
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
    # emotion_detector("Hello how are you")