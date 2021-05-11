from fdd_sdk.client.org import OrgClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 获取个人unionId地址
def get_employee_demo():
    try:
        data = {
            'company': '公司unionId值',
            'offset': '1',
            'size': '10'
        }
        print(OrgClient.get_employee(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取个人信息
def get_add_employee_url_demo():
    try:
        data = {
            'company': '公司unionId值',
            'employeeInfo': {
                'unionId': '员工unionId值'
            }
        }
        print(OrgClient.get_add_employee_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取企业unionId地址
def get_add_sub_company_url_demo():
    try:
        data = {
            'parentCompany': '母公司unionId值',
            'subCompany': '子公司unionId值'
        }
        print(OrgClient.get_add_sub_company_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取企业信息
def get_change_company_major_url_demo():
    try:
        data = {
            'unionId': '子公司或者主体公司unionId值'
        }
        print(OrgClient.get_change_company_major_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 校验账号
def get_child_company_list_demo():
    try:
        data = {
            'company': '公司unionId'
        }
        print(OrgClient.get_child_company_list(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取接入方信息
def remove_sub_company_demo():
    try:
        data = {
            'parentCompany': '母公司unionId值',
            'subCompany': '子公司unionId值'
        }
        print(OrgClient.remove_sub_company(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取开通服务地址
def del_employee_demo():
    try:
        data = {
            'company': '公司unionId值',
            'employeeInfo': {
                'unionId': '员工unionId值'
            }
        }
        print(OrgClient.del_employee(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 批量同步员工数据
def batch_sync_employee_demo():
    try:
        data = {
            'unionId': '公司unionId值',
            'employeeInfos': [
                {
                    'employeeName': '员工姓名',
                    'mobile': '员工手机号',
                    'email': '员工email',
                    'action': 1
                }
            ]
        }
        print(OrgClient.batch_sync_employee(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)

    get_employee_demo()
    get_add_employee_url_demo()
    get_change_company_major_url_demo()
    get_child_company_list_demo()
    get_add_sub_company_url_demo()
    remove_sub_company_demo()
    del_employee_demo()
    batch_sync_employee_demo()
