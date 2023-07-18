import requests

class Apies():
	def __init__(self, name):
		params = {
		"name" : name
		}
		self.params = params
	def age(self):
		return requests.get("https://api.agify.io/", params=self.params).json()['age']
	def pol(self):
		reponase = requests.get("https://api.genderize.io/", params=self.params).json()['gender']
		if reponase == 'male':
			return "мужчина"
		elif reponase == 'female':
			return "женщина"
	# def nationalaze(self):
	# 	reponase = requests.get("https://api.nationalize.io/", params=params).json()['']
	# 	par = {
	# 	"name" : self.params['name'],
	# 	"client" : "x",
	# 	"text" : reponase
	# 	}
	# 	return requests.get("http://translate.google.ru/translate_a/t?client=x&text={textToTranslate}&hl=en&sl=en&tl=ru")
	def job(self):
		reponase = requests.get("https://www.boredapi.com/api/activity").json()['activity']
		par = {
		"name" : self.params['name'],
		"client" : "x",
		"text" : reponase,
		"hl" : "en",
		"sl" : "en",
		"tl" : "ru"
		}
		return requests.get("http://translate.google.ru/translate_a/t")

def ex(name):
	a = Apies(name)
	return f"Возраст : {a.age()},\nПол : {a.pol()},\nЗанятие : {a.job()}"