from fdd_sdk.client.sign_task import SignTaskClient
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

from base_demo import fdd_client
from base_demo import token
from base_demo import user_token


# 利用文件库id创建签署任务
def signtasks_create_by_file_demo():
    try:
        data = {
            'taskSubject': '签署任务编号',
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
                    'mobile': '外部签署人手机号码',
                    'personName': '外部签署人姓名',
                    'companyName': '外部签署人组织名称',
                },
                'signOrder': '203',
                'notice': {
                    'notifyWay': '1',
                    'notifyAddress': '手机号码',
                },
                'fileSigns': [{
                    'fileId': '文件编号',
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
        print(SignTaskClient.signtasks_create_by_file(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 根据模板创建签署任务
def signtasks_create_by_draft_id_demo():
    try:
        data = {
            'taskSubject': '签署任务主题',
            'draftId': '草稿文件编号',
            'status': 'sent',
            'sort': '1',
            'sender': {
                'signWay': '1',
                'signIntendWay': '1',
                'signOrder': '1',
                'templateRoleName': '角色名称',
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
                'templateRoleName': '角色名称',
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
        print(SignTaskClient.signtasks_create_by_draft_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取签署链接
def get_sign_url_demo():
    try:
        data = {
            'taskId': '签署任务编号',
            'unionId': 'unionId值',
            'redirectUrl': '回调通知地址',
            'miniProgramSign': '1'
        }
        print(SignTaskClient.get_sign_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 查询签署详情
def get_task_detail_by_task_id_demo():
    try:
        data = {
            'taskId': '签署任务编号',
            'unionId': 'unionId值'
        }
        print(SignTaskClient.get_task_detail_by_task_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 撤销签署任务
def cancel_demo():
    try:
        data = {
            'taskId': '签署任务编号',
            'remark': '撤销原因'
        }
        print(SignTaskClient.cancel(fdd_client, data))
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
        print(SignTaskClient.get_sent_url(fdd_client, data))
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
        print(SignTaskClient.urge_sign(fdd_client, data))
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
        print(SignTaskClient.get_sign_preview_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 依据原始文件创建签署任务
def create_task_by_file_demo():
    try:
        data = {
            'taskSubject': '签署任务主题',
            'status': 'sent',
            'sort': '1',
            'sender': {
                'unionId': '发送人unionId值'
            },
            'files': [
                {
                    'fileId': '文件编号'
                }
            ],
            'attachments': [
                {
                    'fileId': '附件编号'
                }
            ],
            'signers': [
                {
                    'signer': {
                        'signatory': {
                            'signerId': '签署人unionId值',
                            'seal': {
                                'sealId': '印章编号'
                            }
                        },
                        'corp': {
                            'corpId': '组织unionId',
                            'seal': {
                                'sealId': '印章编号'
                            }
                        },
                        'signAction': {
                            'signWay': 1,
                            'signIntendWay': 1
                        }
                    },
                    'notice': {
                        'notifyWay': 1,
                        'notifyAddres': '通知手机号码'
                    }
                }
            ],
            'externalSigner': {
                'mobile': '外部签署人手机号码',
                'personName': '外部签署人姓名',
                'externalCorp': {
                    'corpName': ''
                }
            },
            'signOrder': '1',
            'signRegions': [
                {
                    'fileId': '文件编号',
                    'signHeres': [
                        {
                            'pageNumber': '0',
                            'xCoordinate': '12.2',
                            'yCoordinate': '152.2'
                        }
                    ]
                }
            ],
            'ccs': [
                {
                    'unionId': 'unionId值',
                    'notice': {
                        'notifyWay': '1',
                        'notifyAddress': '手机号码'
                    }
                }
            ],
            'autoArchive': '1'
        }
        print(SignTaskClient.create_task_by_file(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 创建批量签
def batch_create_by_draft_id_demo():
    try:
        data = {
            'sender': {
                'signIntendWay': '1',
                'unionId': '1'
            },
            'signtasks': [{
                'taskSubject': '签署任务主题',
                'draftId': '草稿编号',
                'sort': '1',
                'sender': {
                    'signWay': '1',
                    'signIntendWay': '1',
                    'signOrder': '1',
                    'templateRoleName': '角色名称',
                    'sealId': ''
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
                }
            }]

        }
        print(SignTaskClient.batch_create_by_draft_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 添加批量签任务
def batch_add_by_draft_id_demo():
    try:
        data = {
            'batchNo': '批次号',
            'signtasks': [{
                'taskSubject': '签署任务主题',
                'draftId': '草稿编号',
                'sort': '1',
                'sender': {
                    'signWay': '1',
                    'signIntendWay': '1',
                    'signOrder': '1',
                    'templateRoleName': '角色名称',
                    'sealId': ''
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
                }
            }]

        }
        print(SignTaskClient.batch_add_by_draft_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 批量签获取签署链接
def batch_get_sign_url_demo():
    try:
        data = {
            'batchNo': '批次号'
        }
        print(SignTaskClient.batch_get_sign_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 根据批次号获取任务信息
def batch_get_signtasks_by_batch_no_demo():
    try:
        data = {
            'batchNo': '批次号'
        }
        print(SignTaskClient.batch_get_signtasks_by_batch_no(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 根据批次号发起
def batch_sent_demo():
    try:
        data = {
            'batchNo': '批次号'
        }
        print(SignTaskClient.batch_sent(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 根据批次号发起
def create_task_by_draft_id_demo():
    try:
        data = {
            'draftId': '草稿编号',
            'taskSubject': '签署任务主题',
            'status': 'sent',
            'sort': '1',
            'sender': {
                'unionId': 'unionId值'
            },
            'signers': [{
                'templateRoleName': '签署角色名称',
                'signer': {
                    'signatory': {
                        'signerId': '签署人的unionId值',
                        'seal': {
                            'sealId': '印章编号'
                        }
                    },
                    'corp': {
                        'corpId': '组织unionId值',
                        'seal': {
                            'sealId': '印章编号'
                        }
                    },
                    'signAction': {
                        'signWay': 1,
                        'signIntendWay': 1
                    },
                    'notice': {
                        'notifyWay': 1,
                        'notifyAddress': '手机号码'
                    }
                },
                'externalSigner': {
                    'mobile': '外部签署人手机号码',
                    'personName': '外部签署人姓名',
                    'externalCorp': {
                        'corpName': '外部组织的名称'
                    }
                },
                'signOrder': 15
            }],
            'ccs': [{
                'unionId': '抄送人unionId值',
                'notice': {
                    'notifyWay': 1,
                    'notifyAddress': '通知手机号码'
                }
            }],
            'autoArchive': 1
        }
        print(SignTaskClient.create_task_by_draft_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取快捷签署链接
def get_quick_sign_url_demo():
    try:
        data = {
            'taskId': '定稿编号',
            'mobile': '外部签署手机号码',
            'redirectUrl': '签署完成重定向地址',
            'miniProgram': '1',
        }
        print(SignTaskClient.get_quick_sign_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 下载签署任务
def download_sign_task_demo():
    try:
        data = {
            'taskId': '签署任务编号',
            'downloadWay': '1'
        }
        res = SignTaskClient.download_sign_task(fdd_client, data)
        with open('D:/签署任务.zip', 'wb') as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


if __name__ == '__main__':
    fdd_client.set_token(token)
    #  如果是第三方应用就设置userToken
    # fdd_client.set_user_token(user_token)
    signtasks_create_by_file_demo()
    signtasks_create_by_draft_id_demo()
    get_sign_url_demo()
    get_task_detail_by_task_id_demo()
    cancel_demo()
    get_sent_url_demo()
    urge_sign_demo()
    get_sign_preview_url_demo()
    create_task_by_file_demo()
    signtasks_create_by_draft_id_demo()
    create_task_by_draft_id_demo()
    get_quick_sign_url_demo()
    download_sign_task_demo()

    batch_create_by_draft_id_demo()
    batch_add_by_draft_id_demo()
    batch_get_sign_url_demo()
    batch_sent_demo()
    batch_get_signtasks_by_batch_no_demo()
