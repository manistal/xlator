
import requests 
import json

API_KEY = 'u7Z1bTQg9kAx6GLlp5Yl5_mF_8mcA8WbYswHaldMCyeY'
API_URL = 'https://gateway.watsonplatform.net/language-translator/api'
AUTH = ('apikey', API_KEY)

"""
## TRANSLATE TEXT ## 
curl -X POST -u "apikey:{apikey}" 
    --header "Content-Type: application/json" 
    --data "{\"text\": [\"Hello, world! \", \"How are you?\"], \"model_id\":\"en-es\"}" 
    "{url}/v3/translate?version=2018-05-01"
"""
def translate_text(input_text, model_id='en-es'):
    headers = { 'Content-Type': 'application/json'}
    data = json.dumps({'text': input_text.split('\n'), 'model_id': model_id})
    rsp = requests.post(f"{API_URL}/v3/translate?version=2018-05-01", data=data, headers=headers, auth=AUTH)
    json_rsp = rsp.json()
    return json_rsp['translations'][0]['translation']

"""
## IDENTIFY ## 
curl -X POST -u "apikey:{apikey}" 
    --header "Content-Type: text/plain" 
    --data "Language Translator translates text from one language to another" 
    "{url}/v3/identify?version=2018-05-01"
"""
def identify_language(input_text):
    headers = { 'Content-Type': 'text/plain'}
    rsp = requests.post(f"{API_URL}/v3/identify?version=2018-05-01", data=input_text, headers=headers, auth=AUTH)
    json_rsp = rsp.json()
    return json_rsp['languages'][0]['language']

def identify_and_translate(input_text, translate_to='en'):
    language = identify_language(input_text)
    return translate_text(input_text, model_id=f"{language}-{translate_to}")

"""
## DOCUMENT TRANSLATE ## 
https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-document-translator-tutorial

This is non blocking... wtf 
"""
