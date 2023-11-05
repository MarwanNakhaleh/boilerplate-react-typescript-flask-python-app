import requests
import pprint

url = "https://mls-router1.p.rapidapi.com/reso/odata/Property"

querystring = {"orderby":"ModificationTimestamp desc","top":"5", "Latitude": "40.742054", "longitude":"-83.769417"}

headers = {
	"Authorization": "Bearer eyJraWQiOiJ4TmlXRnlON1V5OTU5a3hnT3J6ZnJQRGJFdlZDXC8rSGNZQ1RXRlJ1ekJSND0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIxMThwbzByNmkxbzFjY3N1NmVlNGNsMTMydSIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXBpXC9yZWFkIiwiYXV0aF90aW1lIjoxNjk4OTM5ODk1LCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0xLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMV9Zd0VaemdxdzkiLCJleHAiOjE2OTg5NDM0OTUsImlhdCI6MTY5ODkzOTg5NSwidmVyc2lvbiI6MiwianRpIjoiNjAzNjVjOTEtZDI1ZS00ODI1LTgzNDgtZTI3MDc2YTg1NjE5IiwiY2xpZW50X2lkIjoiMTE4cG8wcjZpMW8xY2NzdTZlZTRjbDEzMnUifQ.dNwtGH-Y9KGIz_XE9bgZYORIIf5zcQ9mMWrqTgPinAdU_YoetPdFrh8eF9SlR3Ha6c4hIxxgMQ4R6h7lTd23DCYUK86sI97wL1gkVlBWJEVsunUsYQpVpOQcQsErwwukie6plGduDr68bHqrrSuYC5L7VU61nWKsE04JGviuL6taLrJa_uJFUjCRVB_-kGDhYYEMOj-8IioIMkHAPd1aZhKUuaMptb8kGV2J3h-cmwLtTLilROrt3LEd4-ELMhJO5zQoqFCThP5BapK5NKeZrWoJ53z2LVgflLW0MnpF8MVRKScf_CvHoxAlDbieUdpJvob1ZRxoxWfY5_SRTgZeNw",
	"x-api-key": "a50YsdAcOQ6xyDqVYTzEB57jBqKVYV01MyTD4at6",
	"X-RapidAPI-Key": "ef50fb951cmsh2177aa5c0ae66a4p19902djsnf911b101314f",
	"X-RapidAPI-Host": "mls-router1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.json())
