from fdd_sdk.client.client import FddClient
from fdd_sdk.client.oauth2 import Oauth2Client
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'
try:
    result = Oauth2Client.get_token(fdd_client)
    print('token = %s' % result['data']['accessToken'])
except ClientException as  e:
    print(e)
except ServerException as e:
    print(e)
