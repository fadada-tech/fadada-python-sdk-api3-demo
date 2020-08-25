from fdd_sdk.client.client import FddClient
from fdd_sdk.client.template import TemplateClient
from fdd_sdk.utils.hashs import HashUtils
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'

# 上传企业模板文件
def upload_company_template_file():
    data = {
        'templateInfo': {
            'fileHash': '',
            'fileType': '1',
            'templateId': '模板ID'
        }
    }

    file = open('D:\\合同模板文件.pdf', 'rb')
    data['templateInfo']['fileHash'] = HashUtils.sha256_file_hex('D:\\合同模板文件.pdf')
    print(TemplateClient.upload_company_template_file(fdd_client, token, file, data))


# 修改企业模板信息
def update_company_template():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID',
                'templateName': '测试模板',
                'sortType': '1',
                'templateRemark': '备注信息',
                'targets': [{
                    'targetId': '',
                    'roleName': '乙方',
                    'roleType': '1'
                }]
            }
        }
        print(TemplateClient.update_company_template(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取合同模板控件维护链接
def get_edit_company_template_url():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }
        }
        print(TemplateClient.get_edit_company_template_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除合同模板文件
def del_company_template_file():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板Id',
                'fileId': '文件ID'
            }
        }
        print(TemplateClient.del_company_template_file(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板预览链接
def get_company_template_preview_url():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }
        }
        print(TemplateClient.get_company_template_preview_url(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板列表
def query_company_template_list():
    try:
        data = {
            'queryInfo': {
                'currentPageNo': '1',
                'pageSize': '2',
                'keyword': '关键字'
            }
        }
        print(TemplateClient.query_company_template_list(fdd_client, token, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板文件下载
def download_company_template_file():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }

        }
        res = TemplateClient.download_company_template_file(fdd_client, token, data)
        with open("D:/模板文件.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


upload_company_template_file()
update_company_template()
get_edit_company_template_url()
del_company_template_file()
get_company_template_preview_url()
query_company_template_list()
download_company_template_file()
