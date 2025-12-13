import requests

TOKEN = 'karansinghkaransinghqawsxdrfcftygbhuhnjij'
USERNAME = 'karansinghin1234567890'

parameters = {
    'token':TOKEN,
    'username':USERNAME,
    'agreeTermsOfService':'yes',
    'notMinor':'yes'
}
main_endpoint = 'https://pixe.la/v1/users'

# connection = requests.post(url=main_endpoint, json=parameters)
# print(connection.text)

headers = {
    'X-USER-TOKEN':TOKEN
}

graph_config = {
    'id':'graph1',
    'name': 'pushups graph',
    'unit': 'times',
    'type': 'int',
    'color': 'shibafu'
}

graph_endpoint = f'{main_endpoint}/{USERNAME}/graphs'

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_config = {
    'date':'20251213',
    'quantity': '1'
}

pixel_post_endpoint = f'{graph_endpoint}/graph1'
connection = requests.post(url = pixel_post_endpoint, json= pixel_config, headers=headers)
print(connection.text)


