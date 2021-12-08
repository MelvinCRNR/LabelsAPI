from flask import Flask
from joblib import load

app = Flask(__name__)

clf = load('labels_dump.joblib')

@app.route('/')
def home():
	return 'Sentiment predictor for a text. Please right the sentence you want to test with a \'/\' before in the URL bar. And let the current URL before your text.'

@app.route('/<string:text>')
def predictor(text):
	probas = clf.predict_proba([text])[0]
	if probas[0] > probas [1] and probas[0] > probas[2]:
		return 'hate_speech'
	elif probas[1] > probas [0] and probas[1] > probas[2]:
		return 'neither'
	else:
		return 'offensive language'

	'''return{'hate speech':probas[0],
			'neither':probas[1],
			'offensive_language':probas[2]}'''

	
if __name__ == '__main__':
	app.run(debug=True)
