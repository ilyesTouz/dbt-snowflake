import requests

client_id = '3MVG9vvlaB0y1YsK7Hh513dta_j8CEl6nk3sALfPUxzVm4L.w8T_Td8s9HW0o1VaAr_Yhfqo5vKG6pteVyYDa'

client_secret = 'BD8E506F793BAF1123FA935C6A243DF1E75FEF103B2237B8422515CF2F6E59FD'

redirect_url = 'https://localhost/'

sfdc_user = 'ilyestouzene623-th2g@force.com'

sfdc_pass = 'Chacha291968'

auth_url = 'https://roquette3.my.salesforce.com/services/oauth2/token'
url = 'https://login.salesforce.com/services/oauth2/token'


# get access token
data = {'client_id': client_id, 'client_secret': client_secret,
        'grant_type': 'password', 'username': sfdc_user, 'password': sfdc_pass}
response = requests.post(url, data=data)

json_res = response.json()
print(json_res)

# Access token
access_token = response.json()['access_token']
#access_token = '6Cel800D68000003jWEd88868000000LI6FUWAlMKqpckUDeRcrroPTAaI8krNfP4rsfNEDj7pXF4cWXH5IEx0lHz5Yl5RIqc75ZjFhaUrL'
# Get api info
headers = {'Authorization': 'Bearer ' + access_token}

response_object = requests.get('https://roquette3.my.salesforce.com//services/data/v45.0/sobjects/Lead/listviews', headers=headers)
print(response_object.json())

