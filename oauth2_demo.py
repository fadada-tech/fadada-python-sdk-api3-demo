from fdd_sdk.client.oauth2 import Oauth2Client
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 获取token
def get_token_demo():
    try:
        result = Oauth2Client.get_token(fdd_client)
        token = result['data']['accessToken']
        print('token = %s' % token)
        return token
    except ClientException as  e:
        print(e)
    except ServerException as e:
        print(e)


# 获取授权地址
def get_authorize_url_demo():
    try:
        data = {
            'redirectUrl': '回调通知地址',
            'scope': '1',
            'unionId': 'unionId值'
        }
        print(Oauth2Client.get_authorize_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取自动签授权url
def get_auto_sign_auth_url_demo():
    try:
        data = {
            'redirectUrl': '回调通知地址',
            'unionId': 'unionId值'
        }
        print(Oauth2Client.get_auto_sign_auth_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 取消自动签授权
def cancel_auth_sign_auth_demo():
    try:
        data = {
            'unionId': 'unionId值'
        }
        print(Oauth2Client.cancel_auth_sign_auth(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    get_token_demo()
    fdd_client.set_token(token)
    # 如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    get_authorize_url_demo()
    get_auto_sign_auth_url_demo()
    cancel_auth_sign_auth_demo()
