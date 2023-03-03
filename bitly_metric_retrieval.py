import requests
from datetime import datetime, timedelta

# def get_bitly_metrics(link, access_token):
#     headers = {'Authorization': f'Bearer {access_token}'}
#     params = {'units': '-1'}
#     response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks/summary', headers=headers, params= params)
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         raise Exception(f'Error {response.status_code}: {response.json()["message"]}')

# retrieved_data = get_bitly_metrics('bit.ly/3SIkqNY','454810df060a12329b6d85e4f3b9d7f3a4a2dd60')

# print(retrieved_data)

def get_bitly_metrics(link, access_token):
    end_date = datetime.utcnow().strftime('%Y-%m-%d')
    start_date = (datetime.utcnow() - timedelta(days=30)).strftime('%Y-%m-%d')

    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'unit': 'day', 'units': '30', 'rollup': 'false', 'tz_offset': '0', 'size': '1000'}

    response = requests.get(f'https://api-ssl.bitly.com/v4/bitlinks/{link}/clicks', headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()    # Default response 
        clicks_by_day = {}        # clicks_per_day
        for click in data['link_clicks']:
            click_date_str = click.get('created_at', None)
            if click_date_str is not None:
                dt = datetime.strptime(click['created_at'], '%Y-%m-%dT%H:%M:%S%z')
                clicks_by_day[dt.date()] = click['clicks']
    else:
        raise Exception(f'Error {response.status_code}: {response.json()["message"]} for link {link}')

    return data, clicks_by_day


link = 'bit.ly/3SIkqNY'
access_token = '454810df060a12329b6d85e4f3b9d7f3a4a2dd60'
retrieved_data, clicks_by_day = get_bitly_metrics(link, access_token)

# print(retrieved_data)

print('Clicks by day:')
for date, clicks in clicks_by_day.items():
    print(f'  {date}: {clicks}')
