from fdd_sdk.client.revise_task import ReviseTaskClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 创建定稿任务
def create_revise_task_demo():
    try:
        data = {
            'templateId': '模板编号',
            'finalizeWay': 1,
            'sort': 1,
            'sender': {'unionId': '创建人unionId值'},
            'pageValidate': 1,
            'fillRoles': [
                {
                    'roleName': '角色名称',
                    'externaler': {
                        'mobile': '手机号码',
                        'name': '填写人姓名'
                    },
                    'notice': {
                        'notifyWay': '1',
                        'notifyAddress': '手机号码'
                    },
                    'fillTemplateFiles': [{
                        'fileId': '文件编号',
                        'formFields': '{\'name\':\'年靓\',\'address\':\'年靓\'}'
                    }
                    ]
                },
                {
                    'roleName': '角色名称',
                    'unionId': 'unionId值',
                    'notice': {
                        'notifyWay': '1',
                        'notifyAddress': '手机号码'
                    }
                }
            ],
            'taskSubject': 'ISSP走流程',
            'templateFiles': [
                {'fileId': '文件编号', 'fileName': '签署时文件名'}
            ]
        }
        print(ReviseTaskClient.create_revise_task(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 定稿任务撤销
def cancel_revise_task_demo():
    try:
        data = {
            'taskId': '定稿任务编号'
        }
        print(ReviseTaskClient.cancel_revise_task(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取填充链接
def get_fill_file_url_demo():
    try:
        data = {
            'taskId': '定稿任务编号',
            'roleName': '角色名称'
        }
        print(ReviseTaskClient.get_fill_file_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取定稿任务详请
def revise_task_detail_demo():
    try:
        data = {
            'taskId': '定稿任务编号'
        }
        print(ReviseTaskClient.revise_task_detail(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 接口填充
def save_fill_values_demo():
    try:
        data = {
            'taskId': '定稿任务编号',
            'roleFillValues': [{
                'roleName': '角色名称',
                'fillValues': [{
                    'fileId': '文件编号',
                    'values': '{\'name\':\'年靓\',\'address\':\'年靓\'}'
                }]
            }
            ]
        }
        print(ReviseTaskClient.save_fill_values(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    create_revise_task_demo()
    cancel_revise_task_demo()
    get_fill_file_url_demo()
    revise_task_detail_demo()
    save_fill_values_demo()
