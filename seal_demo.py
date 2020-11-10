from fdd_sdk.client.client import FddClient
from fdd_sdk.client.seal import SealClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'
user_token = '获取到的userToken'


# 上传企业印章
def add_company_seal_demo():
    try:
        data = {
            'sealInfo': {
                'imageHash': '',
                'sealName': ''
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.add_company_seal(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除企业印章
def del_company_seal_demo():
    try:
        data = {
            'sealInfo': {
                'sealId': '印章ID'
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.del_company_seal(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 印章授权
def seal_auth_demo():
    try:
        data = {
            'sealInfo': {
                'sealId': '印章ID'
            },
            'employeeInfo': {
                'unionId': 'unionId值'
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.seal_auth(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 印章取消授权
def cancel_seal_auth_demo():
    try:
        data = {
            'sealInfo': {
                'sealId': '印章ID'
            },
            'employeeInfo': {
                'unionId': 'unionId值'
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.cancel_seal_auth(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业印章列表
def company_seal_list_demo():
    try:
        data = {
            'sealInfo': {
                'loadUnPass': '0'
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.company_seal_list(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 企业印章详请
def company_seal_detail_demo():
    try:
        data = {
            'sealInfo': {
                'sealId': '印章Id'
            },
            'owner': {
                'unionId': ''
            }
        }
        print(SealClient.company_seal_detail(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


fdd_client.set_token(token)
#  如果是第三方应用就设置userToken
# fdd_client.set_user_token(user_token)
add_company_seal_demo()
del_company_seal_demo()
seal_auth_demo()
cancel_seal_auth_demo()
company_seal_list_demo()
company_seal_detail_demo()
