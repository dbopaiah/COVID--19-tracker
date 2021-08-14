import requests

url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api_india"

headers = {
    'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com",
    'x-rapidapi-key': "33f1673efemshe6e0a36c0cea3bfp17fd52jsnb9eb10cfbc0e"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)