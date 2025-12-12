# import requests
# from twilio.rest import Client

# account_sid = '<get from twilio>'
# auth_token = '<get from twilio>'

# parameters = {
#     'lat':<your latitude>,
#     'lon':<your longitude here>,
#     'appid':'<api key here>',
#     'cnt': 4
# }
# connection = requests.get(f'https://api.openweathermap.org/data/2.5/forecast', params=parameters)

# data = connection.json()
# connection.raise_for_status()
# # print(data)
# description = data['list'][0]['weather'][0]['description']
# print(description)

# for i in range(4):
#     will_rain = False
#     id = data['list'][i]['weather'][0]['id']
#     if (id > 699) and (id < 800):
#         will_rain = True
#     client = Client(account_sid, auth_token)

#     if will_rain:
#         text = 'bring an umbrella it will rain'
#     else:
#         text = 'no need for an umbrella it aint gonna rain'
#     message = client.messages \
#         .create(
#         from_='<number from twilio>',
#         to='<your verified number here>',
#         body=text
#         )