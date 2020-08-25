from fdd_sdk.client.client import FddClient
from fdd_sdk.client.employee import EmployeeClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'

# 新增员工
def add_employee_demo():
    try:
        data = {
            'employeeInfo': {
                'unionId': 'unionId值'
            }
        }
        print(EmployeeClient.add_employee(fdd_client, token, data))
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
        print(EmployeeClient.del_employee(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

del_employee_demo()
add_employee_demo()
