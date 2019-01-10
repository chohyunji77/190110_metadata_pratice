import requests
import json
import METADATA

params = {
    'versualFeatures':'Description',
    'language': 'en'
}

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.VISION_KEY
}

data = {
    "url":"https://m.s1campus.co.kr:1543/comm/images/facility/b_lecture1.jpg"
}

res = requests.post('https://koreacentral.api.cognitive.microsoft.com/vision/v2.0/describe',
                params=params, headers=headers, json=data)


res_dict = json.loads(res.text)
txt = res_dict['description']['captions'][0]['text']

params = {
    'api-version':'3.0',
    'from':'en',
    'to':'ko'
}

headers = {
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': METADATA.TRANSLATE_KEY
}

data = [{
    "Text":txt
}]

res = requests.post('https://api.cognitive.microsofttranslator.com/translate',
                params=params, headers=headers, json=data)



res_dict = json.loads(res.text)
result = res_dict[0]['translations'][0]['text']
print(result)
