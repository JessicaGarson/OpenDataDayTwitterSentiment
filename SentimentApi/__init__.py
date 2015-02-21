import requests

ANALYSIS_ENDPOINT = "http://text-processing.com/api/sentiment/"

def analyze_text(text):
	payload = {'text': text}
	response = requests.post(ANALYSIS_ENDPOINT, data=payload)
	decoded_response = response.json()
	positivity_factor = decoded_response['probability']['pos']
	negativity_factor = decoded_response['probability']['neg']
	neutrality_factor = decoded_response['probability']['neutral']

	return_value = 0

	if (neutrality_factor > 0.5):
		pass
	elif (positivity_factor > 0.5):
		return_value = 1
	elif (negativity_factor > 0.5):
		return_value = -1

	return return_value