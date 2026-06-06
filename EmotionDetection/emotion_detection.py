"""
emotion detection
"""
import requests
import json


def emotion_detector(text_to_analyze):
    """
    returnon the emotion response
    """
    url = ('https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    myobj = {"raw_document": {"text": text_to_analyze}}
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header, timeout=5)
    formatted_response = json.loads(response.text)
    emotion = formatted_response["emotionPredictions"][0]["emotion"]
    max = 0.0
    dominant_emotion = None
    for key, item in emotion.items():
        if item > max:
            dominant_emotion = key
            max = item

    emotion["dominant_emotion"] = dominant_emotion

    return emotion
