from fdd_sdk.client.client import FddClient

# fdd_client = FddClient('000003', '30BOgfz4vcEu7h6TjpYPa1EJ',request_url='http://127.0.0.1:8004/api/v3/')
fdd_client = FddClient('FA25444835', 'XONZ3L2ADXEEVLA9CC3AXZVVXYAQ8SDD',
                       request_url='https://sit-gw.fadada.com/api/v3/')
token = '057d2711ba0a4d9fa24d98055a39868f'
user_token = None

from fdd_sdk.client.client import FddClient
from fdd_sdk.client.oauth2 import Oauth2Client
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

# fdd_client = FddClient('appId值', 'appKey值')
result = Oauth2Client.get_token(fdd_client)
print('token = %s' % result['data']['accessToken'])
