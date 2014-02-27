import requests
import urllib
import json

key = ''

def query(query):
	if len(key) > 0:
		headers = {'Authorization': 'Bearer ' + key}
		url = 'https://api.wit.ai/message?q=' + urllib.quote(query)
		text = requests.get(url, headers = headers).text
		try:
			j = json.loads(text)
		except ValueError:
			j = {'error':text}
		return j
	else:
		raise Exception('Invalid key. Set the key by doing wit.key = XXXX')
 
def queryAudio(filename):
	if len(key) > 0:
		wav_file = open(filename, 'rb')
		headers = {'Authorization': 'Bearer ' + key, 'Content-Type': 'audio/wav'}
		url =  'https://api.wit.ai/speech'
		data = wav_file
		text = requests.post(url, headers = headers, data = data).text
		try:
			j = json.loads(text)
		except ValueError:
			j = {'error':text}
		wav_file.close()
		return j
	else:
		raise Exception('Invalid key. Set the key by doing wit.key = XXXX')
