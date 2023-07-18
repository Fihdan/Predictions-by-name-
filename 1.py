import requests

url = "https://deezerdevs-deezer.p.rapidapi.com/search"

querystring = {"q":"eminem"}

headers = {
	"X-RapidAPI-Key": "d9c293e7e2msh80a39985cdfe99ep1fbd7fjsne0cf095f6fee",
	"X-RapidAPI-Host": "deezerdevs-deezer.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())