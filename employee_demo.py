from fdd_sdk.client.client import FddClient
from fdd_sdk.client.employee import EmployeeClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'
user_token = '获取到的userToken'

# 新增员工
def add_employee_demo():
    try:
        data = {
            'employeeInfo': {
                'unionId': 'unionId值'
            }
        }
        print(EmployeeClient.add_employee(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除员工
def del_employee_demo():
    try:
        data = {
            'employeeInfo': {
                'unionId': 'unionId值'
            }
        }
        print(EmployeeClient.del_employee(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

fdd_client.set_token(token)
#  如果是第三方应用就设置userToken
# fdd_client.set_user_token(user_token)
del_employee_demo()
add_employee_demo()
