from fdd_sdk.client.client import FddClient
from fdd_sdk.client.template import TemplateClient
from fdd_sdk.utils.hashs import HashUtils
from fdd_sdk.exception.exceptions import ClientException
from fdd_sdk.exception.exceptions import ServerException

fdd_client = FddClient('appId', 'appKey')
token = '获取后的token'
user_token = '获取到的userToken'

# 上传企业模板文件
def upload_company_template_file_demo():
    data = {
        'templateInfo': {
            'fileHash': '',
            'fileType': '1',
            'templateId': '模板ID'
        }
    }

    file = open('D:\\合同模板文件.pdf', 'rb')
    data['templateInfo']['fileHash'] = HashUtils.sha256_file_hex('D:\\合同模板文件.pdf')
    print(TemplateClient.upload_company_template_file(fdd_client, file, data))


# 修改企业模板信息
def update_company_template_demo():
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
        print(TemplateClient.update_company_template(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取合同模板控件维护链接
def get_edit_company_template_url_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }
        }
        print(TemplateClient.get_edit_company_template_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 删除合同模板文件
def del_company_template_file_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板Id',
                'fileId': '文件ID'
            }
        }
        print(TemplateClient.del_company_template_file(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板预览链接
def get_company_template_preview_url_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }
        }
        print(TemplateClient.get_company_template_preview_url(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板列表
def query_company_template_list_demo():
    try:
        data = {
            'queryInfo': {
                'currentPageNo': '1',
                'pageSize': '2',
                'keyword': '关键字'
            }
        }
        print(TemplateClient.query_company_template_list(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 模板文件下载
def download_company_template_file_demo():
    try:
        data = {
            'templateInfo': {
                'templateId': '模板ID'
            }

        }
        res = TemplateClient.download_company_template_file(fdd_client, data)
        with open("D:/模板文件.zip", "wb") as f:
            f.write(res.content)
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 获取模板详请
def get_template_detail_by_id_demo():
    try:
        data = {
            'templateId': '模板ID',
        }
        print(TemplateClient.get_template_detail_by_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


# 填充模板
def create_by_template_id_demo():
    try:
        data = {
            'templateId': '模板Id',
            'templateFiles': {
                'templateFileId': '模板文件ID',
                'formFields': {
                },
                'documentFileName': '测试请求'
            }
        }
        print(TemplateClient.create_by_template_id(fdd_client, data))
    except ClientException as e:
        print(e.__str__())
    except ServerException as e:
        print(e.__str__())


fdd_client.set_token(token)
#  如果是第三方应用就设置userToken
# fdd_client.set_user_token(user_token)
upload_company_template_file_demo()
update_company_template_demo()
get_edit_company_template_url_demo()
del_company_template_file_demo()
get_company_template_preview_url_demo()
query_company_template_list_demo()
download_company_template_file_demo()
get_template_detail_by_id_demo()
create_by_template_id_demo()
