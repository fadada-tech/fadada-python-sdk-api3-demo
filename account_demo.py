from fdd_sdk.client.client import FddClient
from fdd_sdk.client.account import AccountClient
from datetime import datetime
from fdd_sdk.utils.globals_params import Params
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'


def get_authorize_url_demo():
    try:
        data = {
            'redirectUrl': '回调通知地址',
            'scope': '1',
            'unionId': 'unionId值'
        }
        print(AccountClient.get_authorize_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


def get_person_unionid_url_demo():
    try:
        data = {
            'clientId': '接入方生成的id，需保证应用内唯一，用于关联接入方账号',
            'notice': {
                'notifyWay': '通知方式：1 短信。暂时仅支持短信通知',
                'notifyAddress': '通知地址：手机号，根据notifyWay对应'
            },
            'person': {
                'name': '姓名',
                'identType': '证件类型：目前支持0：身份证； 1：护照； B：港澳居民来往内地通行证, C：台湾居民来往大陆通行证（默认身份证0）',
                'identNo': '证件号码',
                'mobile': '手机号',
                'idPhotoOptional': '身份证正反面照片:0-只需要头像面 1-头像面与国徽面都需要 2-都不需要',
                'backIdCardImgBase64': '身份证背面照base64（不要base64头）',
                'idCardImgBa': '身份证正面照base64 （不要base64头）',
                'bankCardNo': '银行卡号'
            },
            'allowModify': '是否允许用户在认证页面修改所传的个人认证信息：0允许，1不允许。默认允许',
            'authScope': '授权范围 ：暂时仅支持传“1”（实名信息） 。如不传绑定成功后直接跳转到redirectUrl，若不为空，则绑定成功后跳转到授权页面进行授权，授权成功后再跳转回redirectUrl。得到用户授权后可以调用获取个人实名信息，否则无法获取个人用户实名信息',
            'redirectUrl': '操作完成后重定向地址，同时带上unionId，用于接入方绑定用户在法大大的标识',
            'authScheme': '默认为1，三要素补充方案。个人认证方案：0 三要素标准方案， 1 三要素补充方案， 2 四要素标准方案， 3 四要素补充方案， 4 纯三要素方案， 5 纯四要素方案， 6 三要素补充方案（人工审核版）， 7 四要素补充方案（人工审核版）， 9 二要素+人脸识别方案',
            'isMiniProgram': '是否需要小程序配置信息：0不需要，1需要，默认不需要',
        }

        print(AccountClient.get_person_unionid_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


def get_person_info_demo():
    try:
        data = {
            'unionId': 'unionId值'
        }
        print(AccountClient.get_person_info(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


def get_company_unionid_url_demo():
    try:
        clientId = 'clientId' + datetime.now().strftime(Params.TIME_FORMAT)
        data = {
            'clientId': clientId,
            'company': {
                'companyName': '辉辉测试公司',
                'creditNo': '7887827384728347',
                'legalName': '辉辉',
                'creditImageBase64': '',
                'authorizationFileBase64': '',
                'organizationType': ''
            },
            'bank': {
                'bankName': '测试银行',
                'bandBranchName': '测试支行',
                'bankCardNo': '62179048657694',
                'bankProvinceName': '广东省',
                'bankCityName': '深圳市'

            },
            'applicant': {
                'unionId': 'unionID值',
                'applicantType': ''
            },
            'notice': {
                'notifyWay': '1',
                'notifyAddress': '手机号码'
            },
            'authScope': '',
            'redirectUrl': '回调通知地址',
            'allowModify': '',
            'authScheme': '1'
        }
        print(AccountClient.get_company_unionid_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


def get_company_info_demo():
    try:
        data = {
            'unionId': 'unionId值'
        }
        print(AccountClient.get_company_info(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


def check_account_info_demo():
    try:
        data = {
            'mobile': '手机号码',
            'personName': '',
            'companyName': ''
        }
        print(AccountClient.check_account_info(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())

get_authorize_url_demo()
get_person_unionid_url_demo()
get_person_info_demo()
get_company_unionid_url_demo()
get_company_info_demo()
check_account_info_demo()
