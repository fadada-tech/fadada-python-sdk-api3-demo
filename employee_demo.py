from fdd_sdk.client.employee import EmployeeClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


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


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    del_employee_demo()
    add_employee_demo()
