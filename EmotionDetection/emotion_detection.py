import requests
import json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def format_response(response):
    json_response = response.json()
    emotion_scores = json_response["emotionPredictions"][0]["emotion"]
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores['dominant_emotion'] = dominant_emotion
    return emotion_scores

def emotion_detector(text_to_analyze):
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=HEADERS, data=json.dumps(payload))
    return format_response(response)
