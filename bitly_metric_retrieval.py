import requests

def get_bitly_metrics(link, access_token):
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'units': '-1'}
    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary', headers=headers, params= params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f'Error {response.status_code}: {response.json()["message"]}')

retrieved_data = get_bitly_metrics('bit.ly/3SIkqNY','454810df060a12329b6d85e4f3b9d7f3a4a2dd60')

print(retrieved_data)

