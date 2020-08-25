from fdd_sdk.client.client import FddClient
from fdd_sdk.client.sign_task import SignTaskClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'


# 利用文件库id创建签署任务
def signtasks_create_by_file_demo():
    try:
        data = {
            'taskSubject': 'python-sdk测试',
            'status': 'sent',
            'sort': '1',
            'sender': {
                'signOrder': '1',
                'signWay': '1',
                'signIntendWay': '1',
                'notice': {
                    'notifyWay': '1',
                    'notifyAddress': '通知手机号码',
                },
                'fileSigns': [{
                    'fileId': '文件Id',
                    'signHeres': [{
                        'pageNumber': '页数',
                        'xCoordinate': 'x轴坐标',
                        'yCoordinate': 'y轴坐标',
                    }]
                }]
            },
            'files': [{
                'fileId': '1597894422606157715'
            }],
            'signers': [{
                'unionId': 'unionId值',
                'signIntendWay': '',
                'authorizedUnionId': '',
                'externalSigner': {
                    'mobile': '',
                    'personName': '',
                    'companyName': '',
                },
                'signOrder': '203',
                'notice': {
                    'notifyWay': '1',
                    'notifyAddress': '手机号码',
                },
                'fileSigns': [{
                    'fileId': '1597894422606157715',
                    'signHeres': [{
                        'pageNumber': '0',
                        'xCoordinate': '200',
                        'yCoordinate': '200'
                    }]
                }],
            }],
            'autoArchive': '1',
            'taskConfig': ''
        }
        print(SignTaskClient.signtasks_create_by_file(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 根据模板创建签署任务
def signtasks_create_by_draft_id_demo():
    try:
        data = {
            'taskSubject': 'python-sdk',
            'draftId': '1588853378076160059',
            'status': 'sent',
            'sort': '1',
            'sender': {
                'signWay': '1',
                'signIntendWay': '1',
                'signOrder': '1',
                'templateRoleName': 'df',
                'notice': {
                    'notifyWay': '1',
                    'notifyAddress': '手机号码'
                }
            },
            'signers': {
                'unionId': 'unionId值',
                'signIntendWay': '1',
                'authorizedUnionId': '',
                'signOrder': '1',
                'templateRoleName': '1',
                'externalSigner': {
                    'mobile': '手机号码',
                    'personName': '',
                    'companyName': '',
                },
                'notice': {
                    'notifyWay': '1',
                    'notifyAddress': '手机号码'
                },
            },

            'autoArchive': '1',
            'taskConfig': ''
        }
        print(SignTaskClient.signtasks_create_by_draft_id(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署链接
def get_sign_url_demo():
    try:
        data = {
            'taskId': '任务ID',
            'unionId': 'unionId值',
            'redirectUrl': '回调通知地址',
            'miniProgramSign': '1'
        }
        print(SignTaskClient.get_sign_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署详情
def get_task_detail_by_task_id_demo():
    try:
        data = {
            'taskId': '任务ID',
            'unionId': 'unionId值'
        }
        print(SignTaskClient.get_task_detail_by_task_id(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 撤销签署任务
def cancel_demo():
    try:
        data = {
            'taskId': '任务ID',
            'remark': 'df'
        }
        print(SignTaskClient.cancel(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署任务发起链接
def get_sent_url_demo():
    try:
        data = {
            'taskId': '任务ID'
        }
        print(SignTaskClient.get_sent_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 催签
def urge_sign_demo():
    try:
        data = {
            'taskId': '任务ID'
        }
        print(SignTaskClient.urge_sign(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取预览链接
def get_sign_preview_url_demo():
    try:
        data = {
            'taskId': '任务ID',
            'unionId': 'unionId值'
        }
        print(SignTaskClient.get_sign_preview_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


signtasks_create_by_file_demo()
signtasks_create_by_draft_id_demo()
get_sign_url_demo()
get_task_detail_by_task_id_demo()
cancel_demo()
get_sent_url_demo()
urge_sign_demo()
get_sign_preview_url_demo()

