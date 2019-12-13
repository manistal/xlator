
import requests 
import json
import logging

class BluemixLanguageTranslator():
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_auth = ('apikey', api_key)

    def make_bluemixlang_request(self, method, action, headers=None, data=None):
        try:
            return requests.request(method, f"{self.api_url}/v3/{action}?version=2018-05-01", data=data, headers=headers, auth=self.api_auth).json()
        except Exception as e:
            logging.error(f"Failed request to blumix with: URL: {self.api_url}/v3/{action}, DATA: {data}, HEADERS: {headers}")
            raise e

    def translate_text(self, input_text, model_id='en-es'):
        """
        Applies text translation to input_text based on translation model_id passed 
        https://cloud.ibm.com/apidocs/language-translator/language-translator#translate
        input_text -- Text to translate
        model_id -- Translation model to use, string '{source}-{target}' language code 
        returns None if translation not found
        """
        headers = { 'Content-Type': 'application/json'}
        data = json.dumps({'text': input_text, 'model_id': model_id})
        result = self.make_bluemixlang_request('post', 'translate', headers, data)
        return None if 'translations' not in result else result['translations'][0]['translation']

    def identify_language(self, input_text):
        """
        Identifies the language based on source text 
            https://cloud.ibm.com/apidocs/language-translator/language-translator#identify-language
        input_text -- source text to identify language of
        returns None if translation not found
        """
        headers = { 'Content-Type': 'text/plain'}
        result = self.make_bluemixlang_request('post', 'identify', headers, data=input_text.encode('utf-8'))
        return None if 'languages' not in result else result['languages'][0]['language']

    def get_available_language_models(self):
        """
        Returns list of available translation models on bluemix
            https://cloud.ibm.com/apidocs/language-translator/language-translator#list-models
        """
        result = self.make_bluemixlang_request('get', 'models')
        return result['models']

    def get_identifiable_languages(self):
        """
        Returns a list of available languages 
            https://cloud.ibm.com/apidocs/language-translator/language-translator#list-identifiable-languages
        """
        result = self.make_bluemixlang_request('get', 'identifiable_languages')
        return result['languages']

    """
    TODO: Stretch Goal
    def translate_document
        https://cloud.ibm.com/docs/services/language-translator?topic=language-translator-document-translator-tutorial
    """
