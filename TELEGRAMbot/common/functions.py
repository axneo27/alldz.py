import requests

def get_random_dog():
    endpoint = 'https://dog.ceo/api/breeds/image/random'
    response = requests.get(endpoint)
    data = response.json()
    return data['message']

def get_random(category:str):
    endpoint = f'https://api.api-ninjas.com/v1/randomimage?category={category}'
    response = requests.get(endpoint)
    data = response.json()
    return data['message']