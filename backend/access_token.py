import requests

url = "https://mls-router1.p.rapidapi.com/cognito-oauth2/token"

payload = {
	"grant_type": "client_credentials",
	"app_client_id": "118po0r6i1o1ccsu6ee4cl132u"
}
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "", # fill in API jey
	"X-RapidAPI-Host": "mls-router1.p.rapidapi.com"
}

response = requests.post(url, data=payload, headers=headers)

print(response.json())